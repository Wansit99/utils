# 批量转换为jpg图片格式
import os
import sys
from PIL import Image
from shutil import copy

input_folder = r'D:\软考\数据集\1'  # 源文件夹，包含.png格式图片
output_folder = r'D:\软考\数据集\JPEGImages'   # 输出文件夹
# training_data=[]
a = []
b = []
for root, dirs, files in os.walk(input_folder):
    for filename in (x for x in files):
        if filename.endswith('.jpg'):
            filepath = os.path.join(root, filename)

            object_class = filename
            b.append(object_class)
            #print(a)
        else:
            filepath = os.path.join(root, filename)
            object_class = filename
            a.append(object_class)
            #print(b)


for i in a:
    old_path = input_folder + "\\" + str(i)
    i = i.split('.')[0]
    new_path = output_folder + "\\" + str(i) + '.jpg'
    img = Image.open(old_path)
    img = img.convert('RGB')
    img.save(new_path)

for i in b:
    old_path = input_folder + "\\" + str(i)
    new_path = output_folder + "\\" + str(i)
    copy(old_path, new_path)