import os
import random
import xml.etree.ElementTree as ET

clses = []
cls_num = {}
xml_path = r'J:\WeChat Files\wxid_g2m9t9zkcppw21\FileStorage\File\2022-04\Annotations'

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
        if cls not in cls_num.keys():
            cls_num[cls] = 1
        else:
            cls_num[cls] += 1

result = list(set(clses))
print(result)
print(cls_num)
with open('cls_classes.txt',"w") as f:    #设置文件对象
    for i in result:
        f.write(i)
        f.write('\n')