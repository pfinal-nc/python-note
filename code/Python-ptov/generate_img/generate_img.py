from PIL import Image, ImageDraw, ImageFont
import os
import cv2
import numpy as np
import random
import time


def generate_bg_img():
    image = Image.new("RGB", (544, 960), "black")
    draw_table = ImageDraw.Draw(im=image)
    # image.show()
    image.save('bg.png', 'PNG')
    image.close()


def get_text():
    text_list = [];
    with open('data.txt', "r", encoding='utf-8', errors='ignore') as f:
        for string in f.readlines():
            text_list.append(string.split(','))
    return text_list

def generate_img(text="中文", k=1, num=50, last_string=''):
    img = cv2.imdecode(np.fromfile('bg_' + str(random.randint(1, 2)) + '.jpg', dtype=np.uint8), -1)
    x = random.randint(10, 100)
    # print(img.shape)
    y = random.randint(100, img.shape[0] - 200)
    colors = {1: "black", 2: "red", 3: "white"}
    f = 1
    font_size = random.randint(30, 70)
    while f <= num:
        cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
        pilimg = Image.fromarray(cv2img)
        draw = ImageDraw.Draw(pilimg)
        font = ImageFont.truetype("simkai.ttf", font_size + random.randint(1, 2), encoding="utf-8")
        draw.text((x + random.randint(-5, +5), y + random.randint(-5, +5)), text, colors[random.randint(1, 3)],
                  font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
        cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
        cv2.imencode('.jpg', cv2charimg)[1].tofile('image/' + str(k) + "_" + str(f) + ".jpg")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        f += 1


def img_to_video(total):
    # print(total)
    fps = 28
    size = (544, 960)
    name = random.randint(1,1000)
    videowriter = cv2.VideoWriter(str(name) + ".mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, size)
    for f in range(1, 51):
        img_fen = cv2.imread('fen.png')
        videowriter.write(img_fen)
    path = r'image/'
    for x in range(1, total + 1):
        for i in range(1, 51):
            # print(path + str(x) + '_' + str(i) + '.jpg')
            img = cv2.imread(path + str(x) + '_' + str(i) + '.jpg')
            cv2.waitKey(1)
            videowriter.write(img)
    videowriter.release()


def video_to_img():
    mp4 = cv2.VideoCapture("dou.mp4")  # 读取视频
    is_opened = mp4.isOpened()
    fps = mp4.get(cv2.CAP_PROP_FPS)
    print(fps)
    widght = mp4.get(cv2.CAP_PROP_FRAME_WIDTH)  # 获取视频的宽度
    height = mp4.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 获取视频的高度
    print(str(widght) + "x" + str(height))
    i = 0
    while is_opened:
        if i == 10000:  # 截取前10张图片
            break
        else:
            i += 1
        (flag, frame) = mp4.read()
        file_name = "image/" + str(i) + ".jpg"
        print(file_name)
        if flag == True:
            cv2.imwrite(file_name, frame, [cv2.IMWRITE_JPEG_QUALITY])  # 保存图片
