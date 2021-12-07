import os
import xml.etree.ElementTree as ET
import shutil


def convert_annotation(year, image_id):
    in_file = open(os.path.join(VOCdevkit_path, 'VOC%s/Annotations/%s' % (year, image_id)), encoding='utf-8')
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
    VOCdevkit_path = r'D:\软考\VOC07+12+test\VOCdevkit'
    classes = ['car','bottle','person']
    xml_id = []

    if annotation_mode == 0:
        print("Generate txt in ImageSets.")
        xmlfilepath = os.path.join(VOCdevkit_path, 'VOC2007\Annotations')
        saveBasePath = os.path.join(VOCdevkit_path, 'VOC2007\ImageSets\Main')
        temp_xml = os.listdir(xmlfilepath)
        total_xml = []
        for xml in temp_xml:
            if xml.endswith(".xml"):
                total_xml.append(xml)

        for id_xml in total_xml:
            convert_annotation(2007, id_xml)

    or_xml_path = VOCdevkit_path + '\VOC2007\Annotations\\'
    or_img_path = VOCdevkit_path + '\VOC2007\JPEGImages\\'
    new_xml_path = r'G:\VOC自选数据\Annotations\\'
    new_img_path = r'G:\VOC自选数据\JPEGImages\\'

    print(len(xml_id))
    for i in xml_id:
        shutil.copy(or_xml_path+i, new_xml_path+i)
        img_id = i[:-4] + '.jpg'
        shutil.copy(or_img_path + img_id, new_img_path + img_id)



