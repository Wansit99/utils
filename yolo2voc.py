from tqdm import tqdm
import os
from shutil import copy


def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)


dirs = r'pcb/pcb'

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
JPEGImages_dir = os.path.join(work_sapce_dir, "JPEGImages/")
if not os.path.isdir(JPEGImages_dir):
        os.mkdir(JPEGImages_dir)
clear_hidden_files(JPEGImages_dir)
ImageSets_dir = os.path.join(work_sapce_dir, "ImageSets/")
if not os.path.isdir(ImageSets_dir):
        os.mkdir(ImageSets_dir)
Main_dir = os.path.join(ImageSets_dir, "Main/")
if not os.path.isdir(Main_dir):
        os.mkdir(Main_dir)

list_img_path = os.path.join(dirs, 'images')
list_train_img = os.listdir(os.path.join(list_img_path, 'train'))
list_val_img = os.listdir(os.path.join(list_img_path, 'val'))
list_test_img = os.listdir(os.path.join(list_img_path, 'test'))

# for i in tqdm(list_train_img):
#     copy(os.path.join(list_img_path, 'train', i), os.path.join(JPEGImages_dir, i))
#
# for i in tqdm(list_val_img):
#     copy(os.path.join(list_img_path, 'val', i), os.path.join(JPEGImages_dir, i))
#
# for i in tqdm(list_test_img):
#     copy(os.path.join(list_img_path, 'val', i), os.path.join(JPEGImages_dir, i))

ftrainval   = open(os.path.join(Main_dir,'trainval.txt'), 'w')
ftest       = open(os.path.join(Main_dir,'test.txt'), 'w')
ftrain      = open(os.path.join(Main_dir,'train.txt'), 'w')
fval        = open(os.path.join(Main_dir,'val.txt'), 'w')

list_anno_path = os.path.join(dirs, 'Annotations')
list_train_anno = os.listdir(os.path.join(list_anno_path, 'train'))
list_val_anno = os.listdir(os.path.join(list_anno_path, 'val'))
list_test_anno = os.listdir(os.path.join(list_anno_path, 'test'))

for i in tqdm(list_train_anno):
    name = i.split('.')[0] + '\n'
    ftrainval.write(name)
    ftrain.write(name)
    copy(os.path.join(list_anno_path, 'train', i), os.path.join(annotation_dir, i))

for i in tqdm(list_val_anno):
    name = i.split('.')[0] + '\n'
    ftrainval.write(name)
    fval.write(name)
    copy(os.path.join(list_anno_path, 'val', i), os.path.join(annotation_dir, i))

for i in tqdm(list_test_anno):
    name = i.split('.')[0] + '\n'
    ftest.write(name)
    copy(os.path.join(list_anno_path, 'test', i), os.path.join(annotation_dir, i))



ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
print("Generate txt in ImageSets done.")

