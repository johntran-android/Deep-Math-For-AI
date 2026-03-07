import xml.etree.ElementTree as ET
import zipfile
import os
import argparse
import tempfile
import shutil
import uuid

def extract_xml(smm_path, temp_dir):
    with zipfile.ZipFile(smm_path, 'r') as z:
        z.extract("document/mindmap.xml", temp_dir)
    return os.path.join(temp_dir, "document/mindmap.xml")

def analyze_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    stats = {
        "topics": 0,
        "notes": 0,
        "images": 0,
        "embedded_images": 0,
        "relations": 0,
        "attributes_used": set(),
        "topic_attributes_used": set(),
        "tags_used": set()
    }
    
    for elem in root.iter():
        stats["tags_used"].add(elem.tag)
        for attr in elem.attrib:
            stats["attributes_used"].add(f"{elem.tag}@{attr}")
            if elem.tag == "topic":
                stats["topic_attributes_used"].add(attr)
                
    stats["topics"] = len(root.findall(".//topic"))
    stats["notes"] = len(root.findall(".//note"))
    stats["images"] = len(root.findall(".//image"))
    stats["embedded_images"] = len(root.findall(".//embedded-image"))
    stats["relations"] = len(root.findall(".//relation"))
    
    return stats

def compare_structures(real_xml, fake_xml):
    real_stats = analyze_xml(real_xml)
    fake_stats = analyze_xml(fake_xml)
    
    print("="*50)
    print(f"| {'Metric':<25} | {'Real SMM':<10} | {'Fake SMM':<10} |")
    print("="*50)
    print(f"| {'Topics':<25} | {real_stats['topics']:<10} | {fake_stats['topics']:<10} |")
    print(f"| {'Notes':<25} | {real_stats['notes']:<10} | {fake_stats['notes']:<10} |")
    print(f"| {'Images':<25} | {real_stats['images']:<10} | {fake_stats['images']:<10} |")
    print(f"| {'Embedded Images':<25} | {real_stats['embedded_images']:<10} | {fake_stats['embedded_images']:<10} |")
    print(f"| {'Relations':<25} | {real_stats['relations']:<10} | {fake_stats['relations']:<10} |")
    print("="*50)
    
    print("\n--- PHÂN TÍCH THẺ (TAGS) ---")
    real_tags = real_stats["tags_used"]
    fake_tags = fake_stats["tags_used"]
    missing_tags = real_tags - fake_tags
    extra_tags = fake_tags - real_tags
    
    print(f"Real SMM dùng các thẻ: {', '.join(sorted(real_tags))}")
    print(f"Fake SMM dùng các thẻ: {', '.join(sorted(fake_tags))}")
    if missing_tags:
         print(f"[-] Fake SMM THIẾU các thẻ: {', '.join(sorted(missing_tags))}")
    if extra_tags:
         print(f"[+] Fake SMM THỪA các thẻ: {', '.join(sorted(extra_tags))}")
         
    print("\n--- PHÂN TÍCH THUỘC TÍNH CỦA <topic> ---")
    real_attr = real_stats["topic_attributes_used"]
    fake_attr = fake_stats["topic_attributes_used"]
    missing_attr = real_attr - fake_attr
    extra_attr = fake_attr - real_attr
    
    print(f"Real <topic> dùng thuộc tính: {', '.join(sorted(real_attr))}")
    print(f"Fake <topic> dùng thuộc tính: {', '.join(sorted(fake_attr))}")
    if missing_attr:
         print(f"[-] Fake <topic> THIẾU thuộc tính: {', '.join(sorted(missing_attr))}")
         print(f"    (Điều này thường cho thấy đồ họa/style bị lược bỏ như màu sắc, icon, layout)")
    if extra_attr:
         print(f"[+] Fake <topic> THỪA thuộc tính: {', '.join(sorted(extra_attr))}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("real_smm")
    parser.add_argument("fake_smm")
    args = parser.parse_args()
    
    temp_dir = f"temp_compare_{uuid.uuid4().hex[:8]}"
    os.makedirs(temp_dir)
    
    try:
        real_xml = extract_xml(args.real_smm, os.path.join(temp_dir, "real"))
        fake_xml = extract_xml(args.fake_smm, os.path.join(temp_dir, "fake"))
        
        compare_structures(real_xml, fake_xml)
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == '__main__':
    main()
