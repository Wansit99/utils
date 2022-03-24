import os
import xml.etree.ElementTree as ET
import shutil
from tqdm import tqdm


# 从xml中选出指定类别的图片

def convert_annotation(year, image_id):
    in_file = open(os.path.join(VOCdevkit_path, 'VOC2007', 'Annotations', image_id), encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    tag = False
    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') != None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls in classes:
            tag = True
            break

    if tag:
        xml_id.append(image_id)


if __name__ == "__main__":
    annotation_mode = 0
    # 原数据集地址
    VOCdevkit_path = r'./VOCdevkit'
    # 保存在哪里
    new_path = r'./result'
    # 所想要的class
    # classes = ['pn', 'p11', 'pne', 'pl5', 'p12']
    classes = ['person', 'car']
    xml_id = []
    # 保留的百分比
    k = 1

    if annotation_mode == 0:
        print("Generate txt in ImageSets.")
        # xml文件路径
        xmlfilepath = os.path.join(VOCdevkit_path, 'VOC2007', 'Annotations')
        saveBasePath = os.path.join(VOCdevkit_path, 'VOC2007', 'ImageSets', 'Main')
        temp_xml = os.listdir(xmlfilepath)
        total_xml = []
        for xml in temp_xml:
            if xml.endswith(".xml"):
                total_xml.append(xml)

        for id_xml in total_xml:
            convert_annotation(2007, id_xml)

    # 原xml和img的存放路径
    or_xml_path = os.path.join(VOCdevkit_path, 'VOC2007', 'Annotations')
    or_img_path = os.path.join(VOCdevkit_path, 'VOC2007', 'JPEGImages')

    if not os.path.exists(os.path.join(new_path, 'Annotations')):
        os.makedirs(os.path.join(new_path, 'Annotations'))
    if not os.path.exists(os.path.join(new_path, 'JPEGImages')):
        os.makedirs(os.path.join(new_path, 'JPEGImages'))
    if not os.path.exists(os.path.join(new_path, 'ImageSets')):
        os.makedirs(os.path.join(new_path, 'ImageSets'))
        os.makedirs(os.path.join(new_path, 'ImageSets', 'Main'))

    new_xml_path = os.path.join(new_path, 'Annotations')
    new_img_path = os.path.join(new_path, 'JPEGImages')
    print(len(xml_id) * k)
    xml_id = xml_id[:int(len(xml_id) * k)]
    for i in tqdm(xml_id):
        shutil.copy(os.path.join(or_xml_path, i), os.path.join(new_xml_path, i))
        img_id = i[:-4] + '.jpg'
        shutil.copy(os.path.join(or_img_path, img_id), os.path.join(new_img_path, img_id))



