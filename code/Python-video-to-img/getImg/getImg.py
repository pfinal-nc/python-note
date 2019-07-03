import cv2
import math
import os
import config
from PIL import Image
import operator
from functools import reduce
from aip import AipFace
import base64
import imageio


def video_to_img(vide_name):
    mp4 = cv2.VideoCapture("video/" + vide_name)  # 读取视频
    is_opened = mp4.isOpened()
    fps = mp4.get(cv2.CAP_PROP_FPS)
    print(fps)
    widght = mp4.get(cv2.CAP_PROP_FRAME_WIDTH)  # 获取视频的宽度
    height = mp4.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 获取视频的高度
    print(str(widght) + "x" + str(height))
    i = 1
    j = 1
    while is_opened:
        (flag, frame) = mp4.read()
        if i % (int(fps)) == 0:
            file_name = "image/" + str(j) + ".jpg"
            if flag == True:
                cv2.imwrite(file_name, frame, [cv2.INTER_AREA])  # 保存图片
            j += 1
        i += 1
        cv2.waitKey(1)
    mp4.release()


def compare_image(file_image_one, file_image_two):
    image1 = Image.open(file_image_one)
    image2 = Image.open(file_image_two)
    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(
        reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
    # print(differ)
    return differ


def get_image():
    images_list = []
    # print()
    path_list = os.listdir(os.getcwd() + '\image')
    if len(path_list) > 0:
        tmp = []
        for image in path_list:
            tmp.append(int(image.split('.')[0]))
        tmp.sort()
        for i in tmp:
            images_list.append(str(i) + '.jpg')
    # print(path_list)
    return images_list


def get_diff(images_list):
    diff = []
    for image in images_list:
        if (images_list.index(image) + 1) == len(images_list):
            break
        image_next = images_list[images_list.index(image) + 1]
        diff_num = compare_image('image/' + image, 'image/' + image_next)
        # print(diff_num)
        diff_set = {'image_one': image, 'image_two': image_next, 'diff_num': diff_num}
        diff.append(diff_set)
    return diff


def clear_no_face(images_list):
    if len(images_list) > 0:
        for image in images_list:
            check_face_img('image/' + image)


def check_face_img(image_path):
    image_str = get_image_base64(image_path)
    client = AipFace(config.APP_ID, config.APP_KEY, config.SECRET_KEY)
    imageType = "BASE64"
    # print(client.detect(image_str, imageType)['error_code'] != 0)
    if client.detect(image_str, imageType)['error_code'] != 0:
        # print('没有人脸的图片===>' + image_path)
        delete_no_face(image_path)
        # return image_path


def delete_diff(diff_list):
    if len(diff_list) > 0:
        for diff_set in diff_list:
            if diff_set['diff_num'] <= 1000:
                os.remove(os.getcwd() + '\image\\' + diff_set['image_one'])
                print('清除掉了==>' + diff_set['image_one'])


def get_image_base64(image_path):
    with open(image_path, 'rb') as f:  # 以二进制读取图片
        data = f.read()
        encodestr = base64.b64encode(data)  # 得到 byte 编码的数据
        return str(encodestr, 'utf-8')


def delete_no_face(no_face):
    os.remove(os.getcwd() + '\\' + no_face)
    print('清除掉了==>' + no_face)
    return no_face


def generate_gif(path_gif):
    image_list = os.listdir(os.getcwd() + '\\' + path_gif)

    if len(image_list) > 0:
        i = 1
        if len(os.listdir(os.getcwd() + '\\' + path_gif + '\image_Intercept')) <= 0:
            for img in image_list:
                if os.path.isdir(os.getcwd() + '\\' + path_gif + '\\' + img):
                    continue
                image_Intercept(os.getcwd() + '\\' + path_gif + '\\', img)
                i += 1
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name, os.getcwd() + '\\' + path_gif + '\image_Intercept')
    # 截取图片


def image_Intercept(image_path, image):
    img = Image.open(image_path + image)
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度
    x = 0
    y = 0
    w = w - 200
    h = h - 100
    region = img.crop((x, y, x + w, y + h))
    region.save(image_path + '\image_Intercept\\' + image)


def create_gif(image_list, gif_name, image_path):
    frames = []
    print(image_list)
    for image_name in image_list:
        if image_name.endswith('.jpg'):
            print(image_name)
            frames.append(imageio.imread(image_path + '\\' + image_name))
    imageio.mimsave(image_path + '\\' + gif_name, frames, 'GIF', duration=0.2)
