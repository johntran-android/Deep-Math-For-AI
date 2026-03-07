import json
import os
import shutil
import argparse
import zipfile
import xml.etree.ElementTree as ET
from xml.dom import minidom
import uuid

def generate_id():
    # SimpleMind uses integer IDs, but we can try to use UUIDs or a counter
    # StudyBoard gives UUIDs, let's keep a mapping to integers just in case 
    # simplemind balks at string IDs (though typically it might accept strings if they don't contain special chars)
    # Actually, SimpleMind usually uses sequential integers or UUID-like strings. We'll use a counter for safety.
    pass

class SmmExporter:
    def __init__(self):
        self.id_counter = 0
        self.id_mapping = {} # maps StudyBoard ID to SimpleMind ID
        
    def get_sm_id(self, sb_id):
        if sb_id not in self.id_mapping:
            self.id_counter += 1
            self.id_mapping[sb_id] = str(self.id_counter)
        return self.id_mapping[sb_id]

    def build_tree(self, nodes_list):
        nodes_by_id = {n['id']: n for n in nodes_list}
        children_map = {}
        root_nodes = []
        
        for n in nodes_list:
            pid = n.get('parentId')
            if pid and pid in nodes_by_id:
                if pid not in children_map:
                    children_map[pid] = []
                children_map[pid].append(n)
            else:
                root_nodes.append(n)
                
        # Sort children by siblingOrder
        for pid in children_map:
            children_map[pid].sort(key=lambda n: n.get('siblingOrder', 0))
            
        return nodes_by_id, children_map, root_nodes

    def process_node_to_xml(self, sb_node, parent_element, children_map, assets_dir, sm_images_dir):
        sm_id = self.get_sm_id(sb_node['id'])
        sb_parent_id = sb_node.get('parentId')
        sm_parent_id = self.get_sm_id(sb_parent_id) if sb_parent_id else "-1"
        
        # Determine text
        title = (sb_node.get('title') or '').strip()
        if not title and not sb_parent_id:
            title = "Root" # SimpleMind requires root text usually
            
        topic_el = ET.SubElement(parent_element, "topic")
        topic_el.set("id", sm_id)
        topic_el.set("parent", sm_parent_id)
        if title:
            topic_el.set("text", title.replace('\n', '\\N').replace('\r', ''))
            
        # Try to use coordinates if available, otherwise 0
        pos = sb_node.get('position', {})
        topic_el.set("x", str(pos.get('x', 0)))
        topic_el.set("y", str(pos.get('y', 0)))
        
        # Build Note from content & AI analysis
        notes_parts = []
        content = (sb_node.get('content') or '').strip()
        if content:
            notes_parts.append(content)
            
        analysis = sb_node.get('analysis')
        if analysis:
            notes_parts.append("--- AI Feedback ---")
            score = analysis.get('score')
            if score is not None:
                notes_parts.append(f"Score: {score}/100")
            feedback = analysis.get('feedback')
            if feedback:
                notes_parts.append(feedback)
                
        for i, session in enumerate(sb_node.get('reviewSessions', [])):
            notes_parts.append(f"--- Review Session {i+1} ---")
            score = session.get('score')
            if score is not None:
                notes_parts.append(f"Score: {score}/100")
            feedback = session.get('feedback')
            if feedback:
                notes_parts.append(feedback)
                
        # In SimpleMind, notes are wrapped inside <children><text><note>...</note></text></children>
        if notes_parts:
            children_el = ET.SubElement(topic_el, "children")
            text_el = ET.SubElement(children_el, "text")
            # SimpleMind usually gives coordinates to text, we'll just put 0,0
            text_el.set("x", "0.00")
            text_el.set("y", "0.00")
            note_el = ET.SubElement(text_el, "note")
            note_el.set("textfmt", "plain")
            note_el.text = "\n\n".join(notes_parts)
            
        # Process Images
        # Main imageBase64 is considered primary embedded image
        image_path = sb_node.get('imageBase64')
        if image_path:
            real_filename = os.path.basename(image_path)
            src = os.path.join(assets_dir, real_filename)
            if os.path.exists(src):
                # Copy to sm_images_dir
                shutil.copy2(src, os.path.join(sm_images_dir, real_filename))
                # SimpleMind <embedded-image name="..."/>
                img_el = ET.SubElement(topic_el, "embedded-image") 
                img_el.set("name", real_filename)
                
        # Attachments
        for att in sb_node.get('attachments', []):
            if att.get('type') == 'image' and att.get('content'):
                att_filename = os.path.basename(att['content'])
                att_src = os.path.join(assets_dir, att_filename)
                if os.path.exists(att_src):
                    shutil.copy2(att_src, os.path.join(sm_images_dir, att_filename))
                    img_el = ET.SubElement(topic_el, "embedded-image")
                    img_el.set("name", att_filename)
                    
        # Recursively process children
        for child in children_map.get(sb_node['id'], []):
            self.process_node_to_xml(child, parent_element, children_map, assets_dir, sm_images_dir)

    def export(self, input_dir, output_smm_path):
        data_file = os.path.join(input_dir, "data.json")
        assets_dir = os.path.join(input_dir, "assets")
        
        if not os.path.exists(data_file):
            print(f"[ERROR] Cannot find {data_file}")
            return False
            
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not data.get('notebooks'):
            print("[ERROR] No notebooks found in data.json")
            return False
            
        notebook = data['notebooks'][0]
        nodes_list = notebook.get('nodes', [])
        
        nodes_by_id, children_map, root_nodes = self.build_tree(nodes_list)
        
        if not root_nodes:
            print("[ERROR] No root node found")
            return False
            
        root_node = root_nodes[0]
        
        # Prepare working directory for packaging
        pack_dir = os.path.join(input_dir, "sm_pack_temp")
        if os.path.exists(pack_dir):
            shutil.rmtree(pack_dir)
            
        doc_dir = os.path.join(pack_dir, "document")
        images_dir = os.path.join(pack_dir, "images")
        os.makedirs(doc_dir)
        os.makedirs(images_dir)
        
        # Build XML
        simplemind_root = ET.Element("simplemind-mindmaps")
        mindmap_el = ET.SubElement(simplemind_root, "mindmap")
        topics_el = ET.SubElement(mindmap_el, "topics")
        
        # Start recursive processing from root
        self.process_node_to_xml(root_node, topics_el, children_map, assets_dir, images_dir)
        
        # Convert XML to string and form full SimpleMind expected shape
        xml_str = ET.tostring(simplemind_root, encoding='utf-8')
        parsed = minidom.parseString(xml_str)
        pretty_xml = parsed.toprettyxml(indent="    ")
        
        # Fix minidom's XML declaration to be exactly as SimpleMind wants it
        lines = pretty_xml.split('\n')
        if lines[0].startswith('<?xml'):
            lines[0] = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE simplemind-mindmaps>'
            
        final_xml = '\n'.join(lines)
        
        # Write to mindmap.xml
        xml_path = os.path.join(doc_dir, "mindmap.xml")
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(final_xml)
            
        # Zip it up as .smm
        with zipfile.ZipFile(output_smm_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(pack_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, pack_dir)
                    zipf.write(file_path, arcname)
                    
        # Cleanup
        shutil.rmtree(pack_dir)
        print(f"[SUCCESS] Exported to {output_smm_path}")
        return True


def main():
    parser = argparse.ArgumentParser(description="Chuyển đổi StudyBoard (.zip) sang SimpleMind (.smmx)")
    parser.add_argument("input_zip", help="Đường dẫn đến file .zip của StudyBoard")
    parser.add_argument("--output", "-o", help="Đường dẫn file .smmx đầu ra (tùy chọn)")
    args = parser.parse_args()

    input_zip = args.input_zip
    if not os.path.exists(input_zip):
        print(f"[LỖI] Không tìm thấy file {input_zip}")
        return
        
    base_name = os.path.splitext(os.path.basename(input_zip))[0]
    output_smm = args.output if args.output else f"{base_name}_converted.smmx"
    
    # Extract studyboard zip to temp dir
    temp_dir = f"temp_extract_{uuid.uuid4().hex[:8]}"
    os.makedirs(temp_dir, exist_ok=True)
    
    print(f"[*] Đang giải nén {input_zip}...")
    try:
        with zipfile.ZipFile(input_zip, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            
        exporter = SmmExporter()
        print(f"[*] Đang chuyển đổi sang định dạng SimpleMind...")
        exporter.export(temp_dir, output_smm)
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            
if __name__ == '__main__':
    main()
