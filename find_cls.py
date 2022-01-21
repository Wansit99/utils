import os
import random
import xml.etree.ElementTree as ET

clses = []

xml_path = r'C:\Users\wwwwssssww\Desktop\VOC2007\Annotations'

temp_xml        = os.listdir(xml_path)
total_xml       = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)

for name in total_xml:
    in_file = open(os.path.join(xml_path, name), encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        clses.append(cls)

print(list(set(clses)))