import cv2 as cv
import torch
from  matplotlib import pyplot as plt
import numpy as np
import torch.nn.functional as F
import torch.nn as nn
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import os

dark = plt.imread('2015_01386_dark.jpg')
light  = plt.imread('2015_01386.jpg')

output_txt_dir = r'./kk.txt'  # 输出文件夹
f = open(output_txt_dir, 'w')

class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()  # 第一句话，调用父类的构造函数
        np.random.seed(1)
        self.init = torch.tensor(np.random.rand(1,1)).to(torch.float32)
        self.dense = torch.nn.Linear(1, 1)
        output_txt_dir = r'./kk.txt'  # 输出文件夹
        self.f = open(output_txt_dir, 'w+')


    def forward(self, x, y):
        k = F.sigmoid(self.dense(self.init))
        x =  torch.tensor(x).to(torch.float32)
        y =  torch.tensor(y).to(torch.float32)
        self.f.write(str(k.item())+'\n')
        self.f.flush()
        img = k*x + (1-k)*y
        return img

    def __del__(self):
        self.f.close()
        print("析构函数")


net = MyNet()

class LeafData(Dataset):  # 继承Dataset
    def __init__(self):  # __init__是初始化该类的一些基础参数
        self.length = 1
        self.net = net

    def __len__(self):  # 返回整个数据集的大小
        return self.length

    def __getitem__(self, index):  # 根据索引index返回dataset[index]
        return self.net(light, dark)

def my_loss(img):  #@save
    return -torch.var(img)

#net = MyNet()
train_dataset = LeafData()
gen = DataLoader(train_dataset, shuffle=True, batch_size=1, num_workers=1)
trainer = torch.optim.SGD(net.parameters(), lr=0.03)

for i in range(1):
    for i, img in enumerate(train_dataset):
        #img = net(light, dark)
        l = my_loss(img)
        l.backward()
        trainer.step()
        print(l)


