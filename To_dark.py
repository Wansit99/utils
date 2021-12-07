import os
import sys
import numpy as np
from PIL import Image

# txt = []
# with open(r"C:\Users\wwwwssssww\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\ImageSets\Main\test.txt", "r") as f:  # 打开文件
#     for line in f.readlines():
#         line = line.strip('\n')  #去掉列表中每一个元素的换行符
#         #print(line)
#         couple = (line+'_real_A'+'.png',line+'_fake_B'+'.png')
#         txt.append(couple)

input_folder = r'G:\手动变黑img'  # 源文件夹，包含.jpg格式图片
output_folder = r'G:\手动变黑'  # 输出文件夹
a = []
for root, dirs, files in os.walk(input_folder):
    for filename in (x for x in files):

        filepath = os.path.join(root, filename)

        object_class = filename
        a.append(object_class)

for i in a:
    real_path = input_folder + "\\" + str(i)
    img_true = np.array(Image.open(real_path), dtype=np.float32)

    img = img_true * 0.1
    img[img < 0] = 0
    img = Image.fromarray(img.astype('uint8')).convert('RGB')
    new_path = output_folder + "\\" + str(i)
    img.save(new_path)

