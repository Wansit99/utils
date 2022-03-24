import os
import shutil
from pathlib import Path

path = Path(r'H:\project\garbage_sorting\垃圾图片库')
output_path = Path(r'H:\project\garbage_sorting\垃圾图片')

for root, dirs, files in os.walk(path):
    for dir in dirs:
        tag = dir[:4]
        for root_, dirs_, files_ in os.walk(os.path.join(path,dir)):
            for filename in files_:
                file_path = os.path.join(path, dir, filename)
                new_file_path = os.path.join(output_path, tag, filename)
                shutil.copy(file_path, new_file_path)