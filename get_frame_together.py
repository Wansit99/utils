# -*- coding:utf8 -*-
import cv2
import os
import shutil

# 视频文件存放路径
video_path = r''
save_path = os.path.join(video_path, 'frame')
is_exists = os.path.exists(save_path)
if not is_exists:
        os.makedirs(save_path)
        print('path of %s is build' % save_path)
else:
    shutil.rmtree(save_path)
    os.makedirs(save_path)
    print('path of %s already exist and rebuild' % save_path)




def get_frame_from_video(video_name, interval):
    """
    Args:
        video_name:输入视频名字
        interval: 保存图片的帧率间隔
    Returns:
    """

    # 保存图片的路径
    save_path = os.path.join(video_path, 'frame')

    # 开始读视频
    video_capture = cv2.VideoCapture(video_name)
    i = 0
    j = 0

    video_name_tmp = video_name.split('\\')[-1]

    while True:
        success, frame = video_capture.read()
        i += 1
        if i % interval == 0:
            # 保存图片
            j += 1
            save_name = os.path.join(save_path, video_name_tmp[:-4]) + '_' + str(j) + '_' + str(i) + '.jpg'
            cv2.imwrite(save_name, frame)
            print('image of %s is saved' % save_name)
        if not success:
            print('video is all read')
            break


if __name__ == '__main__':
    videos = os.listdir(video_path)
    for i in videos:
        if i.endswith('.mp4'):
            video_name = os.path.join(video_path, i)
            # 每隔10帧抽1帧
            interval = 10
            get_frame_from_video(video_name, interval)