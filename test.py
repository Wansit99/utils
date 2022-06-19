import numpy as np
import pandas as pd
import requests
import torch
import torch.nn as nn

class ChannelAttentionModule(nn.Module):
    def __init__(self, c1, reduction=16):
        super(ChannelAttentionModule, self).__init__()
        mid_channel = c1 // reduction
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)
        self.shared_MLP = nn.Sequential(
            nn.Linear(in_features=c1, out_features=mid_channel),
            nn.ReLU(),
            nn.Linear(in_features=mid_channel, out_features=c1)
        )
        self.sigmoid = nn.Sigmoid()
        # self.act=SiLU()

    def forward(self, x):
        avgout = self.shared_MLP(self.avg_pool(x).view(x.size(0), -1)).unsqueeze(2).unsqueeze(3)
        maxout = self.shared_MLP(self.max_pool(x).view(x.size(0), -1)).unsqueeze(2).unsqueeze(3)
        return self.sigmoid(avgout + maxout)


class SpatialAttentionModule(nn.Module):
    def __init__(self):
        super(SpatialAttentionModule, self).__init__()
        self.conv2d = nn.Conv2d(in_channels=2, out_channels=1, kernel_size=7, stride=1, padding=3)
        # self.act=SiLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avgout = torch.mean(x, dim=1, keepdim=True)
        maxout, _ = torch.max(x, dim=1, keepdim=True)
        out = torch.cat([avgout, maxout], dim=1)
        out = self.sigmoid(self.conv2d(out))
        return out


class CBAM(nn.Module):
    def __init__(self, c1, c2):
        super(CBAM, self).__init__()
        self.channel_attention = ChannelAttentionModule(c1)
        self.spatial_attention = SpatialAttentionModule()

    def forward(self, x):
        out = self.channel_attention(x) * x
        out = self.spatial_attention(out) * out
        return out


class Add(nn.Module):
    def __init__(self, c1):
        super(Add, self).__init__()
        self.channel_attention = ChannelAttentionModule(c1)
    def forward(self, x, y):
        out = self.channel_attention(x) * x + (1-self.channel_attention(x)) * y
        return out


class Add2(nn.Module):
    def __init__(self, c1):
        super(Add2, self).__init__()
        self.weights = 0.5 * torch.ones(1, c1, 1, 1)
    def forward(self, x, y):
        out = self.weights * x + (1- self.weights) * y
        return out

if __name__ == '__main__':
    a = torch.rand(1, 15, 224, 224)
    b = torch.rand(1, 15, 224, 224)

    Add_ = Add2(15)
    result = Add_(a, b)
    print(result.shape)

    cbam = CBAM(15, 15)
    result = cbam(a)
