import os
from shutil import copy
from tqdm import tqdm

xml_path = r'J:\BaiduNetdiskDownload\裂缝数据集\Annotations'
jpg_path = r'J:\BaiduNetdiskDownload\裂缝数据集\images'
new_jpg_path = r'J:\BaiduNetdiskDownload\裂缝数据集\new_images'
xmls = os.listdir(xml_path)

for i in tqdm(xmls):
    old_path = os.path.join(jpg_path, str(i[:-4] + '.jpg'))
    new_path = os.path.join(new_jpg_path, str(i[:-4] + '.jpg'))
    copy(old_path, new_path)
