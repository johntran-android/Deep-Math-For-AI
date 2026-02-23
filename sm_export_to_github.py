import xml.etree.ElementTree as ET
import os
import re
import shutil
import argparse

def process_inline_math(line):
    MATH_PATTERN = re.compile(r'([a-zA-Z]+_[a-zA-Z0-9]+|[Σ∫ΔθπμσΩαβγδε]+|={1,2}|\bVar\b|\bCov\b|\bE_|\bE\b|/|\+|\-)')
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
    text = re.sub(r'\\\*(.*?)\\\*', r'**\1**', text)
    lines = text.split('\n')
    out_lines = []
    MATH_PATTERN = re.compile(r'([a-zA-Z]+_[a-zA-Z0-9]+|[Σ∫ΔθπμσΩαβγδε]+|={1,2}|\bVar\b|\bCov\b|\bE_|\bE\b|/|\+|\-)')
    
    for line in lines:
        if not line.strip():
            out_lines.append("")
            continue
        matches = MATH_PATTERN.findall(line)
        if len(matches) > 3:
            out_lines.append(f"```text\n{line.strip()}\n```")
        elif len(matches) > 0:
            out_lines.append(process_inline_math(line))
        else:
            out_lines.append(line)
    return '\n'.join(out_lines)

def to_snake_case(s):
    s = s.replace('\\N', ' ').replace('\\n', ' ')
    s = re.sub(r'[^\w\s-]', '', s).strip()
    s = re.sub(r'[-\s]+', '_', s).lower()
    if not s:
        s = "untitled"
    return s

def find_image_file(image_name, images_dir):
    if not os.path.exists(images_dir):
        return None
    for f in os.listdir(images_dir):
        if f.startswith(image_name):
            return f
    return None

def process_node(node, level, file_writer, images_dir, assets_output_dir):
    # Xử lý text topic
    topic_text = node['text'].replace('\\N', ' ').replace('\\n', ' ')
    clean_topic = process_inline_math(topic_text)
    
    base_indent = ""
    if level == 2:
        file_writer.write(f"\n## {clean_topic}\n\n")
    elif level == 3:
        file_writer.write(f"\n### {clean_topic}\n\n")
    elif level >= 4:
        indent_spaces = "  " * (level - 4)
        file_writer.write(f"{indent_spaces}- {clean_topic}\n")
        base_indent = indent_spaces + "  "
    
    # Xử lý Note
    for note in node['notes']:
        note_content = process_text_block(note)
        if level >= 4:
            # indent note lines to align with bullet
            note_lines = note_content.split('\n')
            indented_note = '\n'.join([f"{base_indent}{l}" if l.strip() else "" for l in note_lines])
            file_writer.write(f"{indented_note}\n")
        else:
            file_writer.write(f"{note_content}\n\n")
            
    # Xử lý Images
    for img_name in node['images']:
        real_filename = find_image_file(img_name, images_dir)
        if real_filename:
            src_path = os.path.join(images_dir, real_filename)
            dest_path = os.path.join(assets_output_dir, real_filename)
            shutil.copy2(src_path, dest_path)
            
            img_markdown = f"![Image](assets/{real_filename})"
            if level >= 4:
                file_writer.write(f"{base_indent}{img_markdown}\n")
            else:
                file_writer.write(f"{img_markdown}\n\n")

    # Đệ quy cho children
    for child in node['children']:
        process_node(child, level + 1, file_writer, images_dir, assets_output_dir)

def main():
    parser = argparse.ArgumentParser(description="Parse SimpleMind XML to Github Monorepo Markdown")
    parser.add_argument("input_dir", help="Đường dẫn đến thư mục unzip của SimpleMind (chứa document/mindmap.xml)")
    parser.add_argument("output_dir", help="Đường dẫn đến thư mục chứa các Môn học (VD: Github_Repo/)")
    args = parser.parse_args()

    xml_file = os.path.join(args.input_dir, "document", "mindmap.xml")
    images_dir = os.path.join(args.input_dir, "images")
    
    if not os.path.exists(xml_file):
        print(f"[LỖI] Không tìm thấy {xml_file}")
        return

    tree = ET.parse(xml_file)
    root_xml = tree.getroot()
    
    nodes = {}
    for topic in root_xml.findall('.//topic'):
        node_id = topic.get('id')
        try:
            y_val = float(topic.get('y', 0))
        except ValueError:
            y_val = 0.0

        nodes[node_id] = {
            'id': node_id,
            'parent': topic.get('parent'),
            'text': topic.get('text', ''),
            'y': y_val,
            'notes': [],
            'images': [],
            'children': []
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
    for node_id, node in nodes.items():
        parent_id = node['parent']
        if parent_id == '-1':
            root_node = node
        elif parent_id in nodes:
            nodes[parent_id]['children'].append(node)

    for node_id, node in nodes.items():
        node['children'].sort(key=lambda n: n['y'])

    if not root_node:
        print("[LỖI] Không tìm thấy Root Node (parent='-1')")
        return

    # 1. Tạo thư mục môn học
    root_folder_name = to_snake_case(root_node['text'])
    course_output_dir = os.path.join(args.output_dir, root_folder_name)
    assets_output_dir = os.path.join(course_output_dir, "assets")
    os.makedirs(assets_output_dir, exist_ok=True)
    
    print(f"[*] Tạo khóa học: {root_folder_name} tại {course_output_dir}")
    
    # 2. Xử lý các Level 1 -> thực chất là Level 2 (Chapters)
    # Trong file XML, Root Node là A0_CASELLA (Level 0)
    # Con của Root Node là "STATISTICAL INFERENCE - CASELLA" (Level 1)
    # L1 có con là "MỘT SỐ GHI CHÚ CHAPTER 1 - CASELLA" (Level 2)
    # L2 có con là các "Chap 1.1 SET THEORY", "CHAP 1.2.1" (Level 3 - Các Chapter thực sự cần tách)
    # Để an toàn, thay vì fix cứng cấp độ, ta sẽ tách thành file riêng biệt đối với cấp độ CHỨA chữ "Chap" hoặc "CHAP", 
    # Hoặc chuẩn nhất theo cấu trúc mà user gửi: "Các nhánh Cấp 1 (Level 1) của Root Node phải được bóc tách"
    # Nhìn vào XML, Root Node ID=0. Nút L1 ID=1 (STATISTICAL...). Nút L2 ID=2 (MỘT SỐ GHI CHÚ...). Nút L3 ID=3, 10, 20... (Chap 1.1, CHAP 1.2.1,...)
    # Ở phiên bản trước ta đếm nhầm Level. 
    # Cấu trúc thực:
    # Root (0) -> L1 (1) -> L2 (2) -> L3 (3, 10, 20...)
    # User muốn tách các "Chapters". Nhìn tên text, Chapters nằm ở L3.
    # Ta sẽ duyệt xuống L1, duyệt xuống L2, rồi tách mỗi con của L2 thành 1 file.
    
    level1_nodes = root_node['children']
    if not level1_nodes: return
    # Lấy nhánh đầu tiên của Root (VD: STATISTICAL INFERENCE)
    l1_node = level1_nodes[0]
    
    level2_nodes = l1_node['children']
    if not level2_nodes: return
    # Lấy nhánh đầu tiên của L1 (VD: MỘT SỐ GHI CHÚ)
    l2_node = level2_nodes[0]

    # Các con của L2 chính là các Chapters (Chap 1.1, Chap 1.2.1...)
    chapter_nodes = l2_node['children']

    for chap_node in chapter_nodes:
        file_name = to_snake_case(chap_node['text']) + ".md"
        file_path = os.path.join(course_output_dir, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            # Ghi tiêu đề file (H1)
            raw_title = chap_node['text'].replace('\\N', ' ').replace('\\n', ' ')
            f.write(f"# {raw_title}\n")
            
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
                    
            # Xử lý đệ quy các children bên trong Chapter này, bắt đầu từ Level 2 (để ra ## H2)
            for child in chap_node['children']:
                process_node(child, 2, f, images_dir, assets_output_dir)
                
        print(f"  + Tạo file: {file_name}")

    print("\n[✓] Hoàn thành export!")

if __name__ == '__main__':
    main()
