import json
import os
import re
import shutil
import argparse
import zipfile

# ─── Shared text processing utilities (from sync.py) ───

def process_inline_math(line):
    MATH_PATTERN = re.compile(r'([a-zA-Z]+_[a-zA-Z0-9]+|[Σ∫ΔθπμσΩαβγδε]+|={1,2}|\\bVar\\b|\\bCov\\b|\\bE_|\\bE\\b|/|\\+|\\-)')
    words = line.split(' ')
    processed_words = []
    for word in words:
        clean_word = word.strip('.,:;()[]{}')
        if MATH_PATTERN.search(clean_word) and not word.startswith('`') and not word.endswith('`') and '**' not in word:
            processed_words.append(f"`{word}`")
        else:
            processed_words.append(word)
    return " ".join(processed_words)

def process_text_block(text):
    lines = text.split('\n')
    out_lines = []
    MATH_PATTERN = re.compile(r'([a-zA-Z]+_[a-zA-Z0-9]+|[Σ∫ΔθπμσΩαβγδε]+|={1,2}|\\bVar\\b|\\bCov\\b|\\bE_|\\bE\\b|/|\\+|\\-)')
    for line in lines:
        if not line.strip():
            out_lines.append("")
            continue
        matches = MATH_PATTERN.findall(line)
        if len(matches) > 3 and '**' not in line:
            out_lines.append(f"```text\n{line.strip()}\n```")
        elif len(matches) > 0:
            out_lines.append(process_inline_math(line))
        else:
            out_lines.append(line)
    return '\n'.join(out_lines)

def to_snake_case(s):
    s = re.sub(r'[^\w\s-]', '', s).strip()
    s = re.sub(r'[-\s]+', '_', s).lower()
    if not s:
        s = "untitled"
    return s

def smart_title(text):
    if not text: return text
    if any(c.isalpha() for c in text) and text.upper() == text:
        ACRONYMS = {
            'CNN', 'NLP', 'SVM', 'LLM', 'T5', 'RNN', 'ODE', 'PDF', 'CDF', 'MGF', 
            'EX', 'VAR', 'CS231N', 'MIT1801', 'STAT110', 'KNN', 'GLOVEC', 'NMT', 'RLHF',
            'BFGS', 'SR1', 'KKT', 'LDLT',
        }
        words = text.split()
        new_words = []
        for w in words:
            clean_w = w.strip('.,:;()[]{}')
            if clean_w.upper() in ACRONYMS:
                new_words.append(w.upper())
            else:
                new_words.append(w.capitalize())
        return " ".join(new_words)
    return text

# ─── StudyBoard specific logic ───

def build_tree(nodes_list):
    """Build parent→children tree from flat node list with parentId."""
    nodes_by_id = {n['id']: n for n in nodes_list}
    children_map = {}  # parentId → [child nodes], sorted by siblingOrder then y
    root_nodes = []
    
    for n in nodes_list:
        pid = n.get('parentId')
        if pid and pid in nodes_by_id:
            if pid not in children_map:
                children_map[pid] = []
            children_map[pid].append(n)
        else:
            root_nodes.append(n)
    
    # Sort children by siblingOrder first, then by y position
    for pid in children_map:
        children_map[pid].sort(key=lambda n: (n.get('siblingOrder', 0), n.get('position', {}).get('y', 0)))
    
    return nodes_by_id, children_map, root_nodes


def get_depth(node, nodes_by_id):
    """Get depth of a node in the tree."""
    d = 0
    curr = node
    while curr.get('parentId') and curr['parentId'] in nodes_by_id:
        d += 1
        curr = nodes_by_id[curr['parentId']]
    return d


def get_chapter_node(node, nodes_by_id, l1_ids):
    """Find the L1 (chapter) ancestor for any node."""
    curr = node
    while curr:
        if curr['id'] in l1_ids:
            return curr
        pid = curr.get('parentId')
        if pid and pid in nodes_by_id:
            curr = nodes_by_id[pid]
        else:
            break
    return None


def process_sb_node(node, depth, writer, children_map, assets_src_dir, assets_dest_dir, nodes_by_id, l1_ids, stats):
    """Recursively process a StudyBoard node and write Markdown."""
    title = (node.get('title') or '').strip()
    content = (node.get('content') or '').strip()
    node_id = node['id']
    analysis = node.get('analysis')
    image_path = node.get('imageBase64')  # e.g. "assets/img_xxx.png"
    attachments = node.get('attachments', [])
    
    anchor = f'<a id="node-{node_id}"></a>'
    
    # Determine heading vs bullet
    heading_text = title if title else None
    
    if heading_text:
        clean_heading = smart_title(process_inline_math(heading_text))
        if depth <= 2:
            writer.write(f"\n{anchor}\n## {clean_heading}\n\n")
        elif depth == 3:
            writer.write(f"\n{anchor}\n### {clean_heading}\n\n")
        elif depth == 4:
            writer.write(f"\n{anchor}\n#### {clean_heading}\n\n")
        else:
            indent = "  " * (depth - 5)
            writer.write(f"{indent}{anchor}\n")
            writer.write(f"{indent}- **{clean_heading}**\n")

    # ── Image (textbook screenshot) ──
    if image_path:
        real_filename = os.path.basename(image_path)
        src = os.path.join(assets_src_dir, real_filename)
        if os.path.exists(src):
            dest = os.path.join(assets_dest_dir, real_filename)
            shutil.copy2(src, dest)
            img_html = f'<p align="center"><kbd><img src="assets/{real_filename}" width="100%"></kbd></p>'
            writer.write(f"{img_html}\n\n")
            stats['images'] += 1

    # ── Attachments (extra images) ──
    for att in attachments:
        if att.get('type') == 'image' and att.get('content'):
            att_filename = os.path.basename(att['content'])
            att_src = os.path.join(assets_src_dir, att_filename)
            if os.path.exists(att_src):
                att_dest = os.path.join(assets_dest_dir, att_filename)
                shutil.copy2(att_src, att_dest)
                att_html = f'<p align="center"><kbd><img src="assets/{att_filename}" width="100%"></kbd></p>'
                writer.write(f"{att_html}\n\n")
                stats['images'] += 1

    # ── Content (user's study notes) ──
    if content:
        formatted = process_text_block(content)
        note_lines = formatted.split('\n')
        alert_lines = ["> [!NOTE]"] + [f"> {l}" if l.strip() else ">" for l in note_lines]
        writer.write('\n'.join(alert_lines) + "\n\n")
        stats['notes'] += 1

    # ── AI Analysis feedback ──
    if analysis:
        score = analysis.get('score')
        feedback = analysis.get('feedback', '')
        is_accurate = analysis.get('isAccurate')
        
        # Chọn icon dựa theo score
        if score is not None:
            if score >= 90:
                icon = "✅"
            elif score >= 70:
                icon = "⚠️"
            else:
                icon = "❌"
            score_text = f" — {icon} Score: **{score}/100**"
        else:
            score_text = ""
        
        writer.write(f"> [!TIP]\n> **🤖 AI Feedback**{score_text}\n>\n")
        if feedback:
            for fl in feedback.split('\n'):
                writer.write(f"> {fl}\n" if fl.strip() else ">\n")
        writer.write("\n")
        stats['analyses'] += 1

    # ── Review Sessions (oral exam style) ──
    review_sessions = node.get('reviewSessions', [])
    for i, session in enumerate(review_sessions):
        s_score = session.get('score', '?')
        s_feedback = session.get('feedback', '')
        writer.write(f"> [!IMPORTANT]\n> **🎤 Review Session {i+1}** — Score: **{s_score}/100**\n>\n")
        if s_feedback:
            for fl in s_feedback.split('\n'):
                writer.write(f"> {fl}\n" if fl.strip() else ">\n")
        writer.write("\n")

    # Add spacing
    if heading_text or content or image_path or analysis or attachments:
        writer.write("<br>\n\n")

    # ── Recurse into children ──
    for child in children_map.get(node_id, []):
        process_sb_node(child, depth + 1, writer, children_map, assets_src_dir, assets_dest_dir, nodes_by_id, l1_ids, stats)


def process_studyboard(input_dir, output_dir, fallback_name=None):
    """Main processing function for a StudyBoard export."""
    data_file = os.path.join(input_dir, "data.json")
    assets_dir = os.path.join(input_dir, "assets")
    
    if not os.path.exists(data_file):
        print(f"[LỖI] Không tìm thấy {data_file}")
        return None, None, None
    
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data.get('notebooks'):
        print("[LỖI] Không tìm thấy notebooks trong data.json")
        return None, None, None
    
    notebook = data['notebooks'][0]
    notebook_title = notebook.get('title', 'Untitled')
    nodes_list = notebook.get('nodes', [])
    
    print(f"[*] StudyBoard Notebook: {notebook_title} ({len(nodes_list)} nodes)")
    
    # Build tree
    nodes_by_id, children_map, root_nodes = build_tree(nodes_list)
    
    if not root_nodes:
        print("[LỖI] Không tìm thấy root node")
        return None, None, None
    
    root_node = root_nodes[0]
    
    # Output folder
    root_folder_name = to_snake_case(fallback_name if fallback_name else notebook_title)
    course_output_dir = os.path.join(output_dir, root_folder_name)
    
    # Wipe & Rebuild
    if os.path.exists(course_output_dir):
        print(f"[*] Dọn dẹp thư mục cũ: {course_output_dir}")
        shutil.rmtree(course_output_dir)
    
    assets_output_dir = os.path.join(course_output_dir, "assets")
    os.makedirs(assets_output_dir, exist_ok=True)
    
    # L1 nodes = Chapters (direct children of root)
    l1_nodes = children_map.get(root_node['id'], [])
    l1_ids = set(n['id'] for n in l1_nodes)
    
    if not l1_nodes:
        print("[LỖI] Root node không có children (chapters)")
        return None, None, None
    
    print(f"[*] Tìm thấy {len(l1_nodes)} chapters")
    
    generated_files = []
    total_stats = {'total_nodes': len(nodes_list), 'total_notes': 0, 'total_images': 0, 'total_analyses': 0}
    
    for l1_node in l1_nodes:
        chapter_title = (l1_node.get('title') or 'Untitled').strip()
        file_name = to_snake_case(chapter_title) + ".md"
        file_path = os.path.join(course_output_dir, file_name)
        
        stats = {'notes': 0, 'images': 0, 'analyses': 0}
        
        from io import StringIO
        content_buffer = StringIO()
        
        # Process L1's own content first (chapter-level notes/images)
        l1_image = l1_node.get('imageBase64')
        l1_content = (l1_node.get('content') or '').strip()
        l1_attachments = l1_node.get('attachments', [])
        
        if l1_image:
            real_filename = os.path.basename(l1_image)
            src = os.path.join(assets_dir, real_filename)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(assets_output_dir, real_filename))
                content_buffer.write(f'<p align="center"><kbd><img src="assets/{real_filename}" width="100%"></kbd></p>\n\n')
                stats['images'] += 1
        
        for att in l1_attachments:
            if att.get('type') == 'image' and att.get('content'):
                att_filename = os.path.basename(att['content'])
                att_src = os.path.join(assets_dir, att_filename)
                if os.path.exists(att_src):
                    shutil.copy2(att_src, os.path.join(assets_output_dir, att_filename))
                    content_buffer.write(f'<p align="center"><kbd><img src="assets/{att_filename}" width="100%"></kbd></p>\n\n')
                    stats['images'] += 1
        
        if l1_content:
            formatted = process_text_block(l1_content)
            note_lines = formatted.split('\n')
            alert_lines = ["> [!NOTE]"] + [f"> {l}" if l.strip() else ">" for l in note_lines]
            content_buffer.write('\n'.join(alert_lines) + "\n\n")
            stats['notes'] += 1
        
        # Recursively process all children of this chapter
        for child in children_map.get(l1_node['id'], []):
            process_sb_node(child, 2, content_buffer, children_map, assets_dir, assets_output_dir, nodes_by_id, l1_ids, stats)
        
        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            clean_h1 = smart_title(chapter_title)
            f.write(f"# {clean_h1}\n\n")
            f.write(f"📊 **Progress:** `{stats['notes']}` Notes | `{stats['images']}` Screenshots | `{stats['analyses']}` AI Reviews\n\n---\n")
            f.write(content_buffer.getvalue())
        
        content_buffer.close()
        
        total_stats['total_notes'] += stats['notes']
        total_stats['total_images'] += stats['images']
        total_stats['total_analyses'] += stats['analyses']
        
        print(f"  + Tạo file: {file_name} ({stats['notes']} notes, {stats['images']} images, {stats['analyses']} AI reviews)")
        generated_files.append({
            'title': smart_title(chapter_title),
            'path': f"{root_folder_name}/{file_name}",
            'notes': stats['notes'],
            'images': stats['images'],
        })
    
    # Also process root node's own content (e.g. study plan) as a separate file
    root_content = (root_node.get('content') or '').strip()
    root_image = root_node.get('imageBase64')
    if root_content or root_image:
        overview_name = "_overview.md"
        overview_path = os.path.join(course_output_dir, overview_name)
        overview_stats = {'notes': 0, 'images': 0, 'analyses': 0}
        
        with open(overview_path, 'w', encoding='utf-8') as f:
            root_title = smart_title((root_node.get('title') or notebook_title).strip())
            f.write(f"# {root_title}\n\n")
            
            if root_image:
                real_filename = os.path.basename(root_image)
                src = os.path.join(assets_dir, real_filename)
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(assets_output_dir, real_filename))
                    f.write(f'<p align="center"><kbd><img src="assets/{real_filename}" width="100%"></kbd></p>\n\n')
                    overview_stats['images'] += 1
            
            if root_content:
                f.write(f"{process_text_block(root_content)}\n")
                overview_stats['notes'] += 1
        
        print(f"  + Tạo file: {overview_name} (overview)")
        generated_files.insert(0, {
            'title': f"📋 Overview",
            'path': f"{root_folder_name}/{overview_name}",
            'notes': overview_stats['notes'],
            'images': overview_stats['images'],
        })
        total_stats['total_notes'] += overview_stats['notes']
        total_stats['total_images'] += overview_stats['images']
    
    print(f"[✓] Thành công: {len(generated_files)} files được tạo cho {root_folder_name}!\n")
    
    course_name = fallback_name if fallback_name else notebook_title
    return course_name, generated_files, total_stats


def update_readme(repo_dir, all_courses):
    """Update README.md - reused logic from sync.py."""
    readme_path = os.path.join(repo_dir, "README.md")
    
    existing_courses = {}
    intro_text = ""
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            parts = content.split("## 📚 Syllabus / Mục lục")
            intro_text = parts[0]
            
            if len(parts) > 1:
                body = parts[1]
                course_blocks = re.split(r'### 📂 ', body)
                for block in course_blocks:
                    if not block.strip(): continue
                    lines = block.strip().split('\n')
                    header = lines[0]
                    c_name_match = re.search(r'^(.*?) \(', header)
                    if c_name_match:
                        c_name = c_name_match.group(1).strip()
                        existing_courses[c_name] = "### 📂 " + block.strip()
    
    if not intro_text:
        intro_text = """### 🧠 My Deep Math For AI Journal

*Welcome to my personal learning dump.*

---
"""

    print(f"[*] Đang cập nhật README với {len(all_courses)} khoá học mới...")
    for course_name, files in all_courses.items():
        total_notes = sum(f.get('notes', 0) for f in files)
        total_images = sum(f.get('images', 0) for f in files)
        
        course_md = f"### 📂 {course_name} (📝 {total_notes} Notes | 📸 {total_images} Screenshots)\n\n"
        for file in files:
            n_n = file.get('notes', 0)
            n_i = file.get('images', 0)
            tag = " *(pending)*" if (n_n <= 1 and n_i <= 1) else ""
            course_md += f"- [{file['title']}]({file['path']}){tag} — `{n_n}n / {n_i}i` \n"
        
        existing_courses[course_name] = course_md.strip()

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(intro_text.strip() + "\n\n## 📚 Syllabus / Mục lục\n\n")
        for c_name in sorted(existing_courses.keys()):
            f.write(existing_courses[c_name] + "\n\n")
            
    print("[✓] Đã cập nhật xong README.md!")


def main():
    parser = argparse.ArgumentParser(description="Đồng bộ StudyBoard exports vào Github Monorepo")
    parser.add_argument("--repo", default=".", help="Đường dẫn đến Monorepo (mặc định là thư mục hiện tại)")
    parser.add_argument("--export-dir", default="sb_exports", help="Thư mục chứa các file .zip StudyBoard (mặc định ./sb_exports/)")
    args = parser.parse_args()

    repo_dir = args.repo
    exports_dir = os.path.join(repo_dir, args.export_dir)
    
    if not os.path.exists(exports_dir):
        os.makedirs(exports_dir)
        print(f"[*] Đã tạo thư mục {exports_dir}.")
        return

    zip_files = [f for f in os.listdir(exports_dir) if f.endswith('.zip')]
    
    if not zip_files:
        print(f"[*] Không tìm thấy file .zip nào trong {exports_dir}.")
        return
    
    all_courses = {}
    
    for zip_file in zip_files:
        zip_path = os.path.join(exports_dir, zip_file)
        temp_dir = os.path.join(exports_dir, "temp_sb_unzip")
        
        # Lấy tên notebook từ tên file: StudyBoard_<name>_<date>.zip
        # Ví dụ: StudyBoard_numerical_optimization_2026-02-24.zip → numerical_optimization
        base_name = os.path.splitext(zip_file)[0]
        # Bỏ prefix "StudyBoard_" và suffix "_YYYY-MM-DD" nếu có
        fallback = base_name
        if fallback.startswith("StudyBoard_"):
            fallback = fallback[len("StudyBoard_"):]
        # Bỏ date suffix (pattern _YYYY-MM-DD)
        fallback = re.sub(r'_\d{4}-\d{2}-\d{2}$', '', fallback)
        
        print(f"[*] Đang giải nén: {zip_file}...")
        
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        course_name, files, stats = process_studyboard(temp_dir, repo_dir, fallback_name=fallback)
        if course_name and files:
            all_courses[course_name] = files
            print(f"   [Audit] {stats['total_notes']} ghi chú, {stats['total_images']} hình ảnh, {stats['total_analyses']} AI reviews.")
        
        shutil.rmtree(temp_dir)
    
    if all_courses:
        update_readme(repo_dir, all_courses)
        print("\n🏆 STUDYBOARD SYNC HOÀN TẤT!")
    else:
        print("\nKhông có Data để xử lý.")


if __name__ == '__main__':
    main()
