# -*- coding:utf-8 -*-
import os
import cv2

# from spider import xk

if __name__ == '__main__':
    fps = 30
    size = (1920, 1080)
    name = 1
    video_writer = cv2.VideoWriter(str(name) + ".avi", cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
    path = os.path.abspath('image') + '/aa/'
    # print(path)
    # print(os.listdir(path))
    num = 0
    for i in os.listdir(path):
        print(path + i)
        try:
            img = cv2.imread(path + i)
        # print(img)
            cv2.waitKey(100)
            video_writer.write(img)
        except Exception as exc:
            print(exc)
        # if num % 100 == 0:
        #     videowriter = cv2.VideoWriter(str(name) + ".avi", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
        #     name += 1
        # num += 1

    video_writer.release()
