import xml.etree.ElementTree as ET
import os
import random
from shutil import copy
from tqdm import tqdm
import shutil
import cv2

classes = ['defect', 'insulator']
# classes=["ball"]

# 训练集 验证集 比例
train_k = 0.9
val_k = 1.0

random.seed(0)


def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(label_path, xml_path):
    in_file = open(xml_path)
    out_file = open(label_path, 'w')
    #     print(xml_path)
    out_tmp = set()
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    if w <= 0 or h <= 0:
        tmp_img_path = xml_path.split('.')[0].split('/')[-1]
        tmp_img = cv2.imread(os.path.join(dirs, 'JPEGImages', tmp_img_path + '.jpg'))
        h, w, c = tmp_img.shape

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_tmp.add(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    #         out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    for i in out_tmp:
        out_file.write(i)

    in_file.close()
    out_file.close()


wd = os.getcwd()
wd = os.getcwd()

dirs = r'all'
if os.path.isdir(os.path.join(dirs, "labels")):
    shutil.rmtree(os.path.join(dirs, "labels"), True)
if not os.path.isdir(os.path.join(dirs, "labels")):
    os.mkdir(os.path.join(dirs, "labels"))
dir_label = os.path.join(dirs, "labels")
if not os.path.isdir(os.path.join(dir_label, "train")):
    os.mkdir(os.path.join(dir_label, "train"))
if not os.path.isdir(os.path.join(dir_label, "val")):
    os.mkdir(os.path.join(dir_label, "val"))

jpg_dirs = os.path.join(dirs, 'images')
if os.path.isdir(os.path.join(dirs, "images")):
    shutil.rmtree(os.path.join(dirs, "images"), True)
if not os.path.isdir(jpg_dirs):
    os.mkdir(jpg_dirs)
jpg_train_dir = os.path.join(jpg_dirs, 'train')
if not os.path.isdir(jpg_train_dir):
    os.mkdir(jpg_train_dir)
jpg_val_dir = os.path.join(jpg_dirs, 'val')
if not os.path.isdir(jpg_val_dir):
    os.mkdir(jpg_val_dir)

label_dir = os.path.join(dirs, "labels")
clear_hidden_files(label_dir)
train_label_dir = os.path.join(label_dir, "train")
val_label_dir = os.path.join(label_dir, "val")
train_anno_dir = r''

train_file = open(os.path.join(wd, "yolov5_train.txt"), 'w')
val_file = open(os.path.join(wd, "yolov5_val.txt"), 'w')
train_file.close()
val_file.close()
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'a')
val_file = open(os.path.join(wd, "yolov5_val.txt"), 'a')

jpg_dir = os.path.join(dirs, 'JPEGImages')
clear_hidden_files(jpg_dir)
jpg_dir_total = os.listdir(jpg_dir)
random.shuffle(jpg_dir_total)
list_train = jpg_dir_total[:int(len(jpg_dir_total) * train_k * val_k)]
list_val = jpg_dir_total[int(len(jpg_dir_total) * train_k * val_k):]

for i in tqdm(range(0, len(list_train))):
    image_path = os.path.join(jpg_dir, list_train[i])
    voc_path = list_train[i]
    (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
    annotation_name = nameWithoutExtention + '.xml'
    label_name = nameWithoutExtention + '.txt'
    label_path = os.path.join(train_label_dir, label_name)
    xml_path = os.path.join(dirs, 'Annotations', annotation_name)

    train_file.write(image_path + '\n')
    convert_annotation(label_path, xml_path)  # convert label
    new_path = os.path.join(jpg_train_dir, list_train[i])
    copy(image_path, new_path)

for i in tqdm(range(0, len(list_val))):
    image_path = os.path.join(jpg_dir, list_val[i])
    voc_path = list_val[i]
    (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
    annotation_name = nameWithoutExtention + '.xml'
    label_name = nameWithoutExtention + '.txt'
    label_path = os.path.join(val_label_dir, label_name)
    xml_path = os.path.join(dirs, 'Annotations', annotation_name)

    val_file.write(image_path + '\n')
    convert_annotation(label_path, xml_path)  # convert label
    new_path = os.path.join(jpg_val_dir, list_val[i])
    copy(image_path, new_path)

train_file.close()
val_file.close()