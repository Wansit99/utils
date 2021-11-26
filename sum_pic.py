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

input_folder = r'C:\Users\wwwwssssww\Downloads\dark_result'  # 源文件夹，包含.jpg格式图片
output_folder = r'C:\Users\wwwwssssww\Desktop\dark_img'  # 输出文件夹
a = []
for root, dirs, files in os.walk(input_folder):
    for filename in files:
       a.append(filename[:10])
    print(a)

txt = list(set(a))

for i in txt:
    fake_path = input_folder + "\\" + str(i) + '_fake_B.png'
    real_path = input_folder + "\\" + str(i) + '_real_A.png'
    img_fake = np.array(Image.open(fake_path),dtype=np.float32)
    img_true = np.array(Image.open(real_path),dtype=np.float32)

    k = 0.02
    img = (1-k)*img_true +k*img_fake
    img = Image.fromarray(img.astype('uint8')).convert('RGB')
    new_path = i
    new_path = output_folder + "\\" + str(new_path) + '.jpg'
    img.save(new_path)
