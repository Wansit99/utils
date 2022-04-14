import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random
from shutil import copyfile
from tqdm import tqdm
classes = ["bus"]
#classes=["ball"]



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
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(label_path, xml_path):
    in_file = open(xml_path)
    out_file = open(label_path, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    in_file.close()
    out_file.close()

wd = os.getcwd()
wd = os.getcwd()
data_base_dir = os.path.join(wd, "VOCdevkit/")
if not os.path.isdir(data_base_dir):
    os.mkdir(data_base_dir)
work_sapce_dir = os.path.join(data_base_dir, "VOC2007/")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)
annotation_dir = os.path.join(work_sapce_dir, "Annotations/")
if not os.path.isdir(annotation_dir):
        os.mkdir(annotation_dir)
clear_hidden_files(annotation_dir)
yolo_labels_dir = os.path.join(work_sapce_dir, "YOLOLabels/")
if not os.path.isdir(yolo_labels_dir):
        os.mkdir(yolo_labels_dir)
clear_hidden_files(yolo_labels_dir)

dirs = r'E:\annotations_trainval2017\wanted'
if not os.path.isdir(os.path.join(dirs, "labels")):
    os.mkdir(os.path.join(dirs, "labels"))
dir_label = os.path.join(dirs, "labels")
if not os.path.isdir(os.path.join(dir_label, "train")):
    os.mkdir(os.path.join(dir_label, "train"))
if not os.path.isdir(os.path.join(dir_label, "val")):
    os.mkdir(os.path.join(dir_label, "val"))

jpg_dirs = os.path.join(dirs, 'JPEGImages')
jpg_train_dir = os.path.join(jpg_dirs, 'train')
jpg_val_dir = os.path.join(jpg_dirs, 'val')
label_dir = os.path.join(dirs, "labels")
train_label_dir = os.path.join(label_dir, "train")
val_label_dir = os.path.join(label_dir, "val")

train_anno_dir = r''

train_file = open(os.path.join(wd, "yolov5_train.txt"), 'w')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'w')
train_file.close()
test_file.close()
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'a')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'a')
list_train = os.listdir(jpg_train_dir) # list image files
list_val = os.listdir(jpg_val_dir)
prob = random.randint(1, 100)
print("Probability: %d" % prob)
for i in tqdm(range(0,len(list_train))):
    image_path = os.path.join(jpg_train_dir, list_train[i])
    voc_path = list_train[i]
    (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
    annotation_name = nameWithoutExtention + '.xml'
    label_name = nameWithoutExtention + '.txt'
    label_path = os.path.join(train_label_dir, label_name)
    xml_path = os.path.join(dirs, 'Annotations', 'train', annotation_name)

    train_file.write(image_path + '\n')
    convert_annotation(label_path, xml_path) # convert label

for i in tqdm(range(0, len(list_val))):
    image_path = os.path.join(jpg_val_dir, list_val[i])
    voc_path = list_val[i]
    (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
    annotation_name = nameWithoutExtention + '.xml'
    label_name = nameWithoutExtention + '.txt'
    label_path = os.path.join(val_label_dir, label_name)
    xml_path = os.path.join(dirs, 'Annotations', 'val', annotation_name)

    test_file.write(image_path + '\n')
    convert_annotation(label_path, xml_path)  # convert label

train_file.close()
test_file.close()
