from tqdm import tqdm
import os
from shutil import copy

dirs = r'C:\Users\wwwwssssww\Downloads\result (3)\fall'

data_base_dir = os.path.join(dirs, "VOCdevkit/")
work_sapce_dir = os.path.join(data_base_dir, "VOC2007/")
annotation_dir = os.path.join(work_sapce_dir, "Annotations/")
JPEGImages_dir = os.path.join(work_sapce_dir, "JPEGImages/")
ImageSets_dir = os.path.join(work_sapce_dir, "ImageSets/")
Main_dir = os.path.join(ImageSets_dir, "Main/")


