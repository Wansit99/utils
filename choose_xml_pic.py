import os
import xml.etree.ElementTree as ET
import shutil
from tqdm import tqdm

# 从xml中选出指定类别的图片

def convert_annotation(year, image_id):
    in_file = open(os.path.join(VOCdevkit_path, 'Annotations', image_id))
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

    if tag:
        xml_id.append(image_id)


if __name__ == "__main__":
    annotation_mode = 0
    VOCdevkit_path = r'D:\软考\hands'
    new_path = r'D:\软考\new'
    if not os.path.exists(os.path.join(new_path, 'VOC2007')):
        os.makedirs(os.path.join(new_path, 'VOC2007'))
    if not os.path.exists(os.path.join(new_path, 'VOC2007', 'Annotations')):
        os.makedirs(os.path.join(new_path, 'VOC2007', 'Annotations'))
    if not os.path.exists(os.path.join(new_path, 'VOC2007', 'JPEGImages')):
        os.makedirs(os.path.join(new_path, 'VOC2007', 'JPEGImages'))
    if not os.path.exists(os.path.join(new_path, 'VOC2007', 'ImageSets')):
        os.makedirs(os.path.join(new_path, 'VOC2007', 'ImageSets'))
    if not os.path.exists(os.path.join(new_path, 'VOC2007', 'ImageSets', 'Main')):
        os.makedirs(os.path.join(new_path, 'VOC2007', 'ImageSets', 'Main'))



    # 所想要的class
    classes = ['five','four', 'three', 'two','one']
    xml_id = []

    if annotation_mode == 0:
        print("Generate txt in ImageSets.")
        # xml文件路径
        xmlfilepath = os.path.join(VOCdevkit_path, 'Annotations')
        saveBasePath = os.path.join(VOCdevkit_path, 'ImageSets\Main')
        temp_xml = os.listdir(xmlfilepath)
        total_xml = []
        for xml in temp_xml:
            if xml.endswith(".xml"):
                total_xml.append(xml)

        for id_xml in total_xml:
            convert_annotation(2007, id_xml)

    # xml和img的新存放路径
    or_xml_path = os.path.join(VOCdevkit_path, 'Annotations\\')
    or_img_path = os.path.join(VOCdevkit_path, 'JPEGImages\\')
    new_xml_path = os.path.join(new_path, 'VOC2007', 'Annotations\\')
    new_img_path = os.path.join(new_path, 'VOC2007', 'JPEGImages\\')

    print(len(xml_id))
    for i in tqdm(xml_id):
        shutil.copy(or_xml_path + i, new_xml_path + i)
        img_id = i[:-4] + '.jpg'
        shutil.copy(or_img_path + img_id, new_img_path + img_id)



