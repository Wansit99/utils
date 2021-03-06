from xml.etree.ElementTree import ElementTree, Element, parse
import xml.etree.ElementTree as ET
import os
import shutil
from tqdm import tqdm

# A的xml地址
A_path = r'C:\Users\wwwwssssww\Downloads\基于航拍图像的绝缘子缺陷检测方法-1742531216-技术小c\Insulators-main\InsulatorDataSet\Defective_Insulators\labels\defect'
# B的xml地址
B_path = r'C:\Users\wwwwssssww\Downloads\基于航拍图像的绝缘子缺陷检测方法-1742531216-技术小c\Insulators-main\InsulatorDataSet\Defective_Insulators\labels\insulator'
# 合并后的xml地址
Sum_path = r'C:\Users\wwwwssssww\Downloads\基于航拍图像的绝缘子缺陷检测方法-1742531216-技术小c\Insulators-main\InsulatorDataSet\Defective_Insulators\labels\all'

# 格式化
def __indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            __indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


for hole_xml in tqdm(os.listdir(A_path)):
    # 将同名xml合并
    if os.path.exists(os.path.join(B_path,hole_xml)):
        #print('fusing',hole_xml)
        tree_hole = parse(os.path.join(A_path,hole_xml))
        root_hole = tree_hole.getroot()  # annotation

        new_hole = tree_hole

        tree_arm = parse(os.path.join(B_path,hole_xml))
        root_arm = tree_arm.getroot()  # annotation
        object = (tree_arm.findall('object'))
        for i in range(len(object)):
            root_hole.append(object[i])
        __indent(root_hole)
        new_hole.write(os.path.join(Sum_path,hole_xml))
    # 不同名xml复制
    else:
        print('copying',hole_xml)
        shutil.copy(os.path.join(A_path,hole_xml), Sum_path)


# 将不同名xml复制
for arm_xml in tqdm(os.listdir(B_path)):
    if not os.path.exists(os.path.join(Sum_path,arm_xml)):
        #print('copying')
        shutil.copy(os.path.join(B_path, arm_xml), Sum_path)
