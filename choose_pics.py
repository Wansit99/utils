import os
import sys
from PIL import Image

# 从指定的文件夹中，选出txt所指定的图像

txt = []
with open(r"C:\Users\wwwwssssww\Desktop\yolov4\yolov4\VOCdevkit\VOC2007\ImageSets\Main\test.txt", "r") as f:  # 打开文件
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        #print(line)
        txt.append(line)

input_folder = r'C:\Users\wwwwssssww\Desktop\yolov4\yolov4\VOCdevkit\VOC2007\JPEGImages'  # 源文件夹，包含.jpg格式图片
output_folder = r'C:\Users\wwwwssssww\Desktop\choosed'  # 输出文件夹
a = []
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename[:10] in txt:
            a.append(filename)
    print(a)

for i in a:
    old_path = input_folder + "\\" + str(i)
    new_path = output_folder + "\\" + str(i[:10]) + '.jpg'
    img = Image.open(old_path)
    img = img.convert('RGB')
    img.save(new_path)
