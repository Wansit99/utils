# 划分图片和xml

import os
import sys
from PIL import Image
from shutil import copy
from pathlib import Path
from tqdm import tqdm

input_folder = Path(r'D:\软考\手势12345')
new_path = Path(r'D:\软考\hands')
a = []
b = []
for root, dirs, files in os.walk(input_folder):
    for filename in (x for x in files):
        if filename.endswith('.xml'):
            filepath = os.path.join(root, filename)
            object_class = filename
            a.append(object_class)
        else:
            filepath = os.path.join(root, filename)
            object_class = filename
            b.append(object_class)

if not os.path.exists(os.path.join(new_path, 'Annotations')):
    os.makedirs(os.path.join(new_path, 'Annotations'))
if not os.path.exists(os.path.join(new_path, 'JPEGImages')):
    os.makedirs(os.path.join(new_path, 'JPEGImages'))
if not os.path.exists(os.path.join(new_path, 'ImageSets')):
    os.makedirs(os.path.join(new_path, 'ImageSets'))
    os.makedirs(os.path.join(new_path, 'ImageSets', 'Main'))


for i in tqdm(b):
    old_path = os.path.join(input_folder, str(i))
    if old_path.endswith('.jpg'):
        old_path = os.path.join(input_folder, str(i))
        new_path_ = os.path.join(new_path, 'JPEGImages', str(i))
        copy(old_path, new_path_)
    else:
        i = i.split('.')[0]
        new_path_tmp = os.path.join(new_path, 'JPEGImages', str(i)) + '.jpg'
        img = Image.open(old_path)
        img = img.convert('RGB')
        img.save(new_path_tmp)

for i in tqdm(a):
    old_path = os.path.join(input_folder, str(i))
    new_path_tmps = os.path.join(new_path, 'Annotations',str(i))
    copy(old_path, new_path_tmps)