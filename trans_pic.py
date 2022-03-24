# 批量转换为jpg图片格式
import os
import sys
from PIL import Image
from shutil import copy
from pathlib import Path
from tqdm import tqdm

input_folder = Path(r'G:\chrome_download\ssd-pytorch-master_\ssd-pytorch-master\VOCdevkit\VOC2007\JPGEImages')# 源文件夹，包含.png格式图片
output_folder = Path(r'G:\chrome_download\ssd-pytorch-master_\ssd-pytorch-master\VOCdevkit\VOC2007\1')  # 输出文件夹

a = []
b = []
for root, dirs, files in os.walk(input_folder):
    for filename in (x for x in files):
        if filename.endswith('.jpg'):
            filepath = os.path.join(root, filename)
            object_class = filename
            b.append(object_class)
        else:
            filepath = os.path.join(root, filename)
            object_class = filename
            a.append(object_class)

for i in tqdm(a):
    old_path = os.path.join(input_folder, str(i))
    i = i.split('.')[0]
    new_path = os.path.join(output_folder, str(i)) + '.jpg'
    img = Image.open(old_path)
    img = img.convert('RGB')
    img.save(new_path)

for i in tqdm(b):
    old_path = os.path.join(input_folder, str(i))
    new_path = os.path.join(output_folder, str(i))
    copy(old_path, new_path)