import xml.etree.ElementTree as ET
import os
import random
from shutil import copy
from tqdm import tqdm
import shutil
import cv2

# classes = ['pig']
# classes=["ball"]

# 训练集 验证集 测试集比例
train_k = 0.8
val_k = 0.75

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





wd = os.getcwd()
wd = os.getcwd()

dirs = r'C:\Users\wwwwssssww\Desktop\insect'
if os.path.isdir(os.path.join(dirs, "labels")):
    shutil.rmtree(os.path.join(dirs, "labels"), True)
if not os.path.isdir(os.path.join(dirs, "labels")):
    os.mkdir(os.path.join(dirs, "labels"))
dir_label = os.path.join(dirs, "labels")
if not os.path.isdir(os.path.join(dir_label, "train")):
    os.mkdir(os.path.join(dir_label, "train"))
if not os.path.isdir(os.path.join(dir_label, "val")):
    os.mkdir(os.path.join(dir_label, "val"))
    if not os.path.isdir(os.path.join(dir_label, "test")):
        os.mkdir(os.path.join(dir_label, "test"))

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
jpg_test_dir = os.path.join(jpg_dirs, 'test')
if not os.path.isdir(jpg_test_dir):
    os.mkdir(jpg_test_dir)
label_dir = os.path.join(dirs, "labels")
clear_hidden_files(label_dir)
train_label_dir = os.path.join(label_dir, "train")
val_label_dir = os.path.join(label_dir, "val")
test_label_dir = os.path.join(label_dir, "test")
train_anno_dir = r''

train_file = open(os.path.join(wd, "yolov5_train.txt"), 'w')
val_file = open(os.path.join(wd, "yolov5_val.txt"), 'w')
test_file = open(os.path.join(wd, "yolov5_test.txt"), 'w')
train_file.close()
val_file.close()
test_file.close()
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'a')
val_file = open(os.path.join(wd, "yolov5_val.txt"), 'a')
test_file = open(os.path.join(wd, "yolov5_test.txt"), 'a')

jpg_dir = os.path.join(dirs, 'JPEGImages')
clear_hidden_files(jpg_dir)
jpg_dir_total = os.listdir(jpg_dir)
random.shuffle(jpg_dir_total)
list_train = jpg_dir_total[:int(len(jpg_dir_total) * train_k * val_k)]
list_val = jpg_dir_total[int(len(jpg_dir_total) * train_k * val_k): int(len(jpg_dir_total) * train_k)]
list_test = jpg_dir_total[int(len(jpg_dir_total) * train_k):]

for i in tqdm(range(0, len(list_train))):
    image_path = os.path.join(jpg_dir, list_train[i])
    voc_path = list_train[i]
    (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
    annotation_name = nameWithoutExtention + '.txt'
    label_name = nameWithoutExtention + '.txt'
    label_path = os.path.join(train_label_dir, label_name)
    txt_path = os.path.join(dirs, 'Annotations', annotation_name)

    train_file.write(image_path + '\n')
    new_path = os.path.join(jpg_train_dir, list_train[i])
    copy(image_path, new_path)
    copy(txt_path, label_path)

for i in tqdm(range(0, len(list_val))):
    image_path = os.path.join(jpg_dir, list_val[i])
    voc_path = list_val[i]
    (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
    annotation_name = nameWithoutExtention + '.txt'
    label_name = nameWithoutExtention + '.txt'
    label_path = os.path.join(val_label_dir, label_name)
    txt_path = os.path.join(dirs, 'Annotations', annotation_name)

    val_file.write(image_path + '\n')
    new_path = os.path.join(jpg_val_dir, list_val[i])
    copy(image_path, new_path)
    copy(txt_path, label_path)

for i in tqdm(range(0, len(list_test))):
    image_path = os.path.join(jpg_dir, list_test[i])
    voc_path = list_test[i]
    (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
    annotation_name = nameWithoutExtention + '.txt'
    label_name = nameWithoutExtention + '.txt'
    label_path = os.path.join(test_label_dir, label_name)
    txt_path = os.path.join(dirs, 'Annotations', annotation_name)

    test_file.write(image_path + '\n')
    new_path = os.path.join(jpg_test_dir, list_test[i])
    copy(image_path, new_path)
    copy(txt_path, label_path)

train_file.close()
val_file.close()
test_file.close()
