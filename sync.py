import xml.etree.ElementTree as ET
import os
import re
import shutil
import argparse
import zipfile

def process_inline_math(line):
    return line

def process_text_block(text):
    # Chuyển \*nội dung\* thành **nội dung** (Bold)
    # Xử lý cả trường hợp nội dung nằm trên nhiều dòng và xóa khoảng trắng thừa ở sát dấu ngoặc để Markdown render chuẩn
    def fix_bold(m):
        content = m.group(1).strip()
        content = content.replace('\\n', ' ').replace('\\N', ' ')
        return f"**{content}**"
    
    text = re.sub(r'\\\*\s*(.*?)\s*\\\*', fix_bold, text, flags=re.DOTALL)
    return text

def to_snake_case(s):
    s = s.replace('\\N', ' ').replace('\\n', ' ')
    s = re.sub(r'[^\w\s-]', '', s).strip()
    s = re.sub(r'[-\s]+', '_', s).lower()
    if not s:
        s = "untitled"
    # Truncate to avoid "File name too long" errors (max 255 on most systems, but we use 100 for safety)
    return s[:100]

def smart_title(text):
    if not text: return text
    # Chỉ xử lý nếu toàn bộ là CHỮ HOA (không tính số và ký tự đặc biệt)
    # Regex: Kiểm tra xem có ít nhất 1 chữ cái và không có chữ thường nào
    if any(c.isalpha() for c in text) and text.upper() == text:
        ACRONYMS = {
            'CNN', 'NLP', 'SVM', 'LLM', 'T5', 'RNN', 'ODE', 'PDF', 'CDF', 'MGF', 
            'EX', 'VAR', 'CS231N', 'MIT1801', 'STAT110', 'KNN', 'GLOVEC', 'NMT', 'RLHF'
        }
        words = text.split()
        new_words = []
        for w in words:
            # Loại bỏ ký tự đặc biệt quanh từ để check acronym
            clean_w = w.strip('.,:;()[]{}')
            if clean_w.upper() in ACRONYMS:
                new_words.append(w.upper())
            else:
                new_words.append(w.capitalize())
        return " ".join(new_words)
    return text

def extract_smm_file(smm_path, extract_to):
    with zipfile.ZipFile(smm_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def find_image_file(image_name, images_dir):
    if not os.path.exists(images_dir):
        return None
    for f in os.listdir(images_dir):
        if f.startswith(image_name):
            return f
    return None

def process_node(node, level, file_writer, images_dir, assets_output_dir):
    n_notes = len(node['notes'])
    n_images = len(node['images'])
    
    # Dùng ID của node làm mỏ neo tàng hình để link nhảy đích xác tới Pixel này
    anchor = f'<a id="node-{node["id"]}"></a>'
    
    # Xử lý text topic
    raw_topic = node['text']
    topic_text = raw_topic.replace('\\N', ' ').replace('\\n', ' ')
    base_indent = "  " * (level - 4) + "  " if level >= 4 else ""
    
    if topic_text.strip():
        # Smart Heading Detection: Nếu node ở Level 2-3 mà có xuống dòng (\N) hoặc quá dài (>100 ký tự)
        # Ta sẽ tách: Dòng đầu làm Heading, toàn bộ nội dung làm Note block.
        is_heavy_heading = (level <= 3) and ('\\N' in raw_topic or len(topic_text) > 100)
        
        if is_heavy_heading:
            first_line = raw_topic.split('\\N')[0].strip()
            clean_heading = smart_title(process_inline_math(first_line.replace('\\n', ' ')))
            
            if level <= 2:
                file_writer.write(f"\n{anchor}\n## {clean_heading}\n\n")
            else:
                file_writer.write(f"\n{anchor}\n### {clean_heading}\n\n")
            
            # Đẩy toàn bộ nội dung (đã format math) vào một Note block đặc biệt ngay dưới tiêu đề
            formatted_content = process_text_block(raw_topic.replace('\\N', '\n').replace('\\n', '\n'))
            content_lines = formatted_content.split('\n')
            alert_lines = ["> [!NOTE]"] + [f"> {l}" if l.strip() else ">" for l in content_lines]
            file_writer.write('\n'.join(alert_lines) + "\n\n")
        else:
            clean_topic = smart_title(process_inline_math(topic_text))
            if level <= 2:
                file_writer.write(f"\n{anchor}\n## {clean_topic}\n\n")
            elif level == 3:
                file_writer.write(f"\n{anchor}\n### {clean_topic}\n\n")
            elif level >= 4:
                indent_spaces = "  " * (level - 4)
                file_writer.write(f"{indent_spaces}{anchor}\n")
                file_writer.write(f"{indent_spaces}- {clean_topic}\n")
                base_indent = indent_spaces + "  "
    else:
        # Nếu nhánh ko có text nhưng có nội dung khác (ảnh/note/link), ta vẫn chèn mỏ neo
        if node['notes'] or node['images'] or node.get('crosslinks', []):
            if level >= 4:
                file_writer.write(f"{base_indent}{anchor}\n")
            else:
                file_writer.write(f"{anchor}\n\n")
        
    # Xử lý Images TRƯỚC (để ảnh sách hiện ra trước khi giải thích)
    for img_name in node['images']:
        real_filename = find_image_file(img_name, images_dir)
        if real_filename:
            src_path = os.path.join(images_dir, real_filename)
            dest_path = os.path.join(assets_output_dir, real_filename)
            shutil.copy2(src_path, dest_path)
            
            img_html = f'<p align="center"><kbd><img src="assets/{real_filename}" width="100%"></kbd></p>'
            
            if level >= 4:
                file_writer.write(f"{base_indent}{img_html}\n")
            else:
                file_writer.write(f"{img_html}\n\n")

    # Xử lý Crosslinks (Relations) NGAY SAU HÌNH, TRƯỚC NOTE
    for link_text, link_url in node.get('crosslinks', []):
        crosslink_md = f"🔗 **Related:** [{link_text}]({link_url})"
        if level >= 4:
            file_writer.write(f"{base_indent}{crosslink_md}\n\n")
        else:
            file_writer.write(f"{crosslink_md}\n\n")

    # Xử lý Note SAU CÙNG (để giải thích nằm dưới ảnh và link)
    for note in node['notes']:
        note_content = process_text_block(note)
        note_lines = note_content.split('\n')
        
        # Bọc Note trong GitHub Alert (khung nền xám xanh nhạt, bo tròn)
        alert_lines = ["> [!NOTE]"] + [f"> {l}" if l.strip() else ">" for l in note_lines]
        
        if level >= 4:
            indented_note = '\n'.join([f"{base_indent}{l}" for l in alert_lines])
            file_writer.write(f"{indented_note}\n\n")
        else:
            alert_content = '\n'.join(alert_lines)
            file_writer.write(f"{alert_content}\n\n")
            
    # Thêm khoảng trống nhỏ (Padding) sau khi xong 1 cụm Text+Note+Image+Crosslink
    if topic_text.strip() or node['notes'] or node['images'] or node.get('crosslinks', []):
        file_writer.write(f"{base_indent}<br>\n\n")

    # Đệ quy cho children
    next_level = level + 1 if topic_text.strip() else level
    for child in node['children']:
        cn, ci = process_node(child, next_level, file_writer, images_dir, assets_output_dir)
        n_notes += cn
        n_images += ci
    
    return n_notes, n_images

def process_mindmap(input_dir, output_dir, fallback_name=None):
    xml_file = os.path.join(input_dir, "document", "mindmap.xml")
    images_dir = os.path.join(input_dir, "images")
    
    if not os.path.exists(xml_file):
        print(f"[LỖI] Không tìm thấy {xml_file} trong {input_dir}")
        return None, None, None

    tree = ET.parse(xml_file)
    root_xml = tree.getroot()
    
    nodes = {}
    for topic in root_xml.findall('.//topic'):
        node_id = topic.get('id')
        try:
            y_val = float(topic.get('y', 0))
        except ValueError:
            y_val = 0.0

        # Lấy text: Ưu tiên attribute 'text', nếu ko có thì tìm tag con <text>
        # SimpleMind sometimes uses <text> child with CDATA or plain text
        node_text = (topic.get('text') or "").strip()
        if not node_text:
            text_tag = topic.find('./text')
            if text_tag is not None:
                node_text = (text_tag.text or "").strip()
                if not node_text:
                    # Try text of children of text tag (if any)
                    node_text = "".join(text_tag.itertext()).strip()

        nodes[node_id] = {
            'id': node_id,
            'parent': topic.get('parent'),
            'text': node_text,
            'y': y_val,
            'notes': [],
            'images': [],
            'children': [],
            'crosslinks': []
        }
        for note in topic.findall('.//note'):
            if note.text:
                nodes[node_id]['notes'].append(note.text)
        for img in topic.findall('.//image'):
            if img.get('name'):
                nodes[node_id]['images'].append(img.get('name'))
        for emb_img in topic.findall('.//embedded-image'):
            if emb_img.get('name'):
                nodes[node_id]['images'].append(emb_img.get('name'))

    root_node = None
    all_roots = []
    for node_id, node in nodes.items():
        parent_id = node['parent']
        if parent_id == '-1':
            all_roots.append(node)
        elif parent_id in nodes:
            nodes[parent_id]['children'].append(node)
    
    # Pick the one with text or the first one
    for r in all_roots:
        if r['text']: 
            root_node = r
            break
    if not root_node and all_roots:
        root_node = all_roots[0]

    for node_id, node in nodes.items():
        node['children'].sort(key=lambda n: n['y'])

    # Parse cross-links (relations) - Two-way link mapping
    crosslinks = {}
    for rel in root_xml.findall('.//relation'):
        src = rel.get('source')
        tgt = rel.get('target')
        if src and tgt and src in nodes and tgt in nodes:
            if src not in crosslinks:
                crosslinks[src] = []
            if tgt not in crosslinks:
                crosslinks[tgt] = []
            
            # Map bi-directional so A<->B
            if tgt not in crosslinks[src]:
                crosslinks[src].append(tgt)
            if src not in crosslinks[tgt]:
                crosslinks[tgt].append(src)
            
    # Function to find the owning file (L3 node) for any given node to build relative URLs
    def get_owning_file_node(node_id):
        curr = node_id
        while curr in nodes:
            parent_id = nodes[curr]['parent']
            if parent_id in nodes and nodes[parent_id]['parent'] == '1':
                return nodes[curr] # L3 node
            if parent_id == '-1': break
            curr = parent_id
        return None

    # Attach processed crosslinks directly to nodes
    for src_id, targets in crosslinks.items():
        for tgt_id in targets:
            tgt_file_node = get_owning_file_node(tgt_id)
            if tgt_file_node:
                tgt_filename = to_snake_case(tgt_file_node['text']) + ".md"
                
                # Try to find the actual text of the target node or its closest readable parent
                tgt_text = ""
                curr_tgt = tgt_id
                while curr_tgt in nodes:
                    txt = nodes[curr_tgt]['text'].replace('\\N', ' ').strip()
                    if txt:
                        tgt_text = txt
                        break
                    curr_tgt = nodes[curr_tgt]['parent']
                
                if not tgt_text: tgt_text = "Related Topic"
                
                # Dùng ID thực tế của Node làm Hash để nhắm bắn cực kỳ chính xác (pixel-perfect)
                anchor = f"node-{tgt_id}"
                
                # Only keep unique links
                link_tuple = (tgt_text, f"{tgt_filename}#{anchor}")
                if link_tuple not in nodes[src_id]['crosslinks']:
                    nodes[src_id]['crosslinks'].append(link_tuple)

    if not root_node:
        print("[LỖI] Không tìm thấy Root Node (parent='-1')")
        return None, None, None

    # Vị trí Cấu trúc: Root (0) -> L1 (1) -> L2 (2 - Các thư mục Chương) -> L3 (3 - Các sub-chapter)
    # NẾU có fallback_name, ta dùng nó làm folder name để tránh bị trùng tiêu đề bên trong
    course_title = root_node['text']
    root_folder_name = to_snake_case(fallback_name if fallback_name else course_title)
    print(f"   [Debug] Root Node Text: '{course_title}' -> Folder: '{root_folder_name}'")
    course_output_dir = os.path.join(output_dir, root_folder_name)
    
    # Cơ chế WIPE & REBUILD
    if os.path.exists(course_output_dir):
        print(f"[*] Dọn dẹp thư mục cũ: {course_output_dir}")
        shutil.rmtree(course_output_dir)
    
    assets_output_dir = os.path.join(course_output_dir, "assets")
    os.makedirs(assets_output_dir, exist_ok=True)
    
    print(f"[*] Đang parse khoá học: {root_folder_name} vào {course_output_dir}")
    
    level1_nodes = root_node['children']
    if not level1_nodes: return None, None, None
    
    # Một số mindmap có 1 node trung gian (Level 1), một số ném Chapter ra ngay dưới Root.
    # Ta sẽ chọn level chứa nhiều con nhất (thường là danh sách Chapter)
    if len(level1_nodes) == 1 and len(level1_nodes[0]['children']) >= 2:
        level2_nodes = level1_nodes[0]['children']
    else:
        # Nếu Root đẻ ra nhiều con luôn (như MIT 1806), thì chính đám con đó là Chapters
        level2_nodes = level1_nodes

    # Thu thập Audit Stats để User an tâm không bị sót data
    stats = {
        'total_nodes': len(nodes),
        'total_notes': sum(len(n['notes']) for n in nodes.values()),
        'total_images': sum(len(n['images']) for n in nodes.values()),
        'total_crosslinks': sum(len(n.get('crosslinks', [])) for n in nodes.values()) // 2 # Chia 2 vì lưu 2 chiều
    }

    generated_files = []

    # Duyệt TẤT CẢ các nhánh Chapters
    for l2_node in level2_nodes:
        # Nếu nhánh này có con, tức là cấu trúc Chapter -> Sub-chapter
        # Nếu nhánh này ko có con nhưng có nội dung, thì chính nó là 1 file
        if l2_node['children'] and len(l2_node['children']) > 1:
            chapter_nodes = l2_node['children']
        else:
            chapter_nodes = [l2_node]
        
        for chap_node in chapter_nodes:
            # Bỏ qua các node rỗng
            if not chap_node['text'].strip():
                continue

            # Dùng first_line cho filename khi text dài hoặc có xuống dòng (\N), giữ nguyên nếu ngắn và 1 dòng
            chap_raw = chap_node['text']
            chap_first_line = chap_raw.split('\\N')[0].split('\\n')[0].strip()
            needs_trim = '\\N' in chap_raw or '\\n' in chap_raw or len(chap_first_line) > 60
            chap_name_for_file = chap_first_line if needs_trim else chap_raw.strip()
            file_name = to_snake_case(chap_name_for_file) + ".md"
            file_path = os.path.join(course_output_dir, file_name)
            
            # Tính toán stats cho chapter này
            chap_notes = len(chap_node['notes'])
            chap_images = len(chap_node['images'])
            
            # Temporary buffer to store content so we can count depth-first
            from io import StringIO
            content_buffer = StringIO()
            
            for child in chap_node['children']:
                cn, ci = process_node(child, 2, content_buffer, images_dir, assets_output_dir)
                chap_notes += cn
                chap_images += ci
                
            with open(file_path, 'w', encoding='utf-8') as f:
                # Ghi tiêu đề file (H1) — dùng toàn bộ text (kể cả mô tả dài)
                raw_title = chap_node['text'].replace('\\N', ' ').replace('\\n', ' ')
                clean_h1 = smart_title(raw_title)
                f.write(f"# {clean_h1}\n\n")
                
                # Thanh tiến độ (Progress Bar)
                f.write(f"📊 **Progress:** `{chap_notes}` Notes | `{chap_images}` Screenshots\n\n---\n")
                
                # Ghi Note / Image của Chapter Level (nếu có)
                for note in chap_node['notes']:
                    f.write(f"\n{process_text_block(note)}\n")
                for img_name in chap_node['images']:
                    real_filename = find_image_file(img_name, images_dir)
                    if real_filename:
                        src_path = os.path.join(images_dir, real_filename)
                        dest_path = os.path.join(assets_output_dir, real_filename)
                        shutil.copy2(src_path, dest_path)
                        f.write(f"\n![Image](assets/{real_filename})\n")
                        
                # Ghi tiếp phần nội dung đã render từ buffer
                f.write(content_buffer.getvalue())
            
            content_buffer.close()

            # Title cho README: lấy first_line nếu text dài hoặc nhiều dòng, giữ nguyên nếu không
            chap_name_for_title = chap_first_line if needs_trim else chap_raw.strip()
            short_title = smart_title(chap_name_for_title.replace('\\N', ' ').replace('\\n', ' '))
                    
            print(f"  + Tạo file: {file_name} ({chap_notes} notes, {chap_images} images)")
            generated_files.append({
                'title': short_title,
                'path': f"{root_folder_name}/{file_name}",
                'notes': chap_notes,
                'images': chap_images
            })

    print(f"[✓] Thành công: {len(generated_files)} bài viết được khởi tạo cho {root_folder_name}!\n")
    return (fallback_name if fallback_name else root_node['text'].replace('\\N', ' ')), generated_files, stats

def update_readme(repo_dir, all_courses):
    readme_path = os.path.join(repo_dir, "README.md")
    
    # 1. Đọc nội dung cũ để lấy Intro và giữ lại các khoá học không có trong đợt quét này
    existing_courses = {}
    intro_text = ""
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Tách phần intro (đến trước Syllabus)
            parts = content.split("## 📚 Syllabus / Mục lục")
            intro_text = parts[0]
            
            # Parse các khoá học cũ (Dạng ### 📂 CourseName)
            if len(parts) > 1:
                body = parts[1]
                # Regex tìm block của từng Course
                course_blocks = re.split(r'### 📂 ', body)
                for block in course_blocks:
                    if not block.strip(): continue
                    lines = block.strip().split('\n')
                    header = lines[0] # "CourseName (stats)"
                    # Lấy tên khoá học sạch (trước dấu ngoặc đơn)
                    c_name_match = re.search(r'^(.*?) \(', header)
                    if c_name_match:
                        c_name = c_name_match.group(1).strip()
                        existing_courses[c_name] = "### 📂 " + block.strip()
    
    # 2. Chuẩn bị Intro mặc định nếu file mới tinh
    if not intro_text:
        intro_text = """### 🧠 My Deep Math For AI Journal

*Welcome to my personal learning dump.*

*Đây không phải là một cuốn giáo trình Toán hoàn hảo hay bách khoa toàn thư sửa sai cho tác giả. Đây đơn giản là **nhật ký bóc tách (deconstruction nhật ký)** của một gã đang vật lộn với những khái niệm Toán hạng nặng đằng sau AI (Casella, Numerical Optimization...).*

*Cách học của tôi là dùng Feynman Technique đập nát từng định lý, công thức thô cứng trong sách thành "tiếng người" dễ hiểu nhất đối với tôi. Bạn sẽ thấy rất nhiều câu như "Khoan, dừng lại một giây phân tích đoạn này đã...", vì tôi tin rằng không có Blackbox nào không thể mở ra được.*

*Và dĩ nhiên, nó chứa góc nhìn cá nhân nên chắc chắn sẽ có sạn. But hey, it shows my thinking process and sweat!*

---
"""

    # 3. Render các khoá học MỚI vào buffer (Ghi đè nếu đã tồn tại)
    print(f"[*] Đang cập nhật README với {len(all_courses)} khoá học mới...")
    for course_name, files in all_courses.items():
        total_notes = sum(f.get('notes', 0) for f in files)
        total_images = sum(f.get('images', 0) for f in files)
        
        course_md = f"### 📂 {course_name} (📝 {total_notes} Notes | 📸 {total_images} Screenshots)\n\n"
        for file in files:
            # Tag low content chapters
            n_n = file.get('notes', 0)
            n_i = file.get('images', 0)
            tag = " *(pending)*" if (n_n <= 1 and n_i <= 1) else ""
            course_md += f"- [{file['title']}]({file['path']}){tag} — `{n_n}n / {n_i}i` \n"
        
        existing_courses[course_name] = course_md.strip()

    # 4. Ghi đè lại toàn bộ file
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(intro_text.strip() + "\n\n## 📚 Syllabus / Mục lục\n\n")
        # Sắp xếp: sb_exports (không có prefix A0_/A1_) lên đầu, sm_exports alphabetical sau
        def readme_sort_key(c_name):
            upper = c_name.upper()
            is_sm = upper.startswith('A0_') or upper.startswith('A1_')
            return (1 if is_sm else 0, c_name.lower())

        for c_name in sorted(existing_courses.keys(), key=readme_sort_key):
            f.write(existing_courses[c_name] + "\n\n")
            
    print("[✓] Đã cập nhật xong README.md (Merging completed)!")


def main():
    parser = argparse.ArgumentParser(description="Tự động đồng bộ SimpleMind (.smm) vào Github Monorepo")
    parser.add_argument("--repo", default=".", help="Đường dẫn đến Monorepo (mặc định là thư mục hiện tại)")
    parser.add_argument("--export-dir", default="sm_exports", help="Thư mục chứa các file .smm zip (mặc định ./sm_exports/)")
    args = parser.parse_args()

    repo_dir = args.repo
    exports_dir = os.path.join(repo_dir, args.export_dir)
    
    if not os.path.exists(exports_dir):
        os.makedirs(exports_dir)
        print(f"[*] Đã tạo thư mục {exports_dir}. Hãy copy file .smm vào đây cho các lần sau!")

    all_courses = {}

    smm_files = [f for f in os.listdir(exports_dir) if f.endswith('.smm') or f.endswith('.smmx')]
    
    if not smm_files:
        print(f"[*] Không tìm thấy file .smm nào trong {exports_dir}.")
        return
    else:
        for smm_file in smm_files:
            smm_path = os.path.join(exports_dir, smm_file)
            temp_extract_dir = os.path.join(exports_dir, "temp_unzip")
            # Lấy tên file không có đuôi làm fallback name
            fallback_course_name = os.path.splitext(smm_file)[0]
            
            print(f"[*] Đang giải nén: {smm_file}...")
            
            if os.path.exists(temp_extract_dir):
                shutil.rmtree(temp_extract_dir)
            os.makedirs(temp_extract_dir)
            
            extract_smm_file(smm_path, temp_extract_dir)
            
            course_name, files, stats = process_mindmap(temp_extract_dir, repo_dir, fallback_name=fallback_course_name)
            if course_name and files:
                all_courses[course_name] = files
                print(f"   [Audit] {stats['total_notes']} ghi chú, {stats['total_images']} hình ảnh, {stats['total_crosslinks']} liên kết.")
                
            shutil.rmtree(temp_extract_dir)

    if all_courses:
        update_readme(repo_dir, all_courses)
        print("\n🏆 QUÁ TRÌNH SYNC ĐÃ HOÀN TẤT XUẤT SẮC!")
    else:
        print("\nKhông có Data để xử lý.")

if __name__ == '__main__':
    main()
