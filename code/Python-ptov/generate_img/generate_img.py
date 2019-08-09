from PIL import Image, ImageDraw, ImageFont
import os
import cv2
import numpy as np
import random
import time
import config
from aip import AipSpeech
from struct import *
from moviepy.editor import *
from moviepy.audio.fx import all
import requests
import time
import hashlib
import base64


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
        font = ImageFont.truetype("font/ukai.ttc", font_size + random.randint(1, 2),
                                  encoding="utf-8")
        draw.text((x + random.randint(-5, +5), y + random.randint(-5, +5)), text, colors[random.randint(1, 3)],
                  font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
        cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
        cv2.imencode('.jpg', cv2charimg)[1].tofile('image/' + str(k) + "_" + str(f) + ".jpg")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        f += 1


def img_to_video(total, radio):
    # print(open('auido_%s.mp3' % str(radio)))
    fps = 28
    size = (544, 960)
    name = random.randint(1, 1000)
    try:
        videowriter = cv2.VideoWriter(str(name) + ".mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, size)
        for f in range(1, 20):
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
        time.sleep(1)
        print("video audio merge!!!!!")
        audioclip = AudioFileClip('auido_%s.mp3' % str(radio))
        print(str(name) + ".mp4")
        videoclip = VideoFileClip(str(name) + ".mp4")
        # print(videoclip)
        videoclip2 = videoclip.set_audio(audioclip)
        video = CompositeVideoClip([videoclip2])
        video.write_videofile('video/' + str(name) + str(random.randint(1, 10)) + ".mp4", codec='mpeg4', fps=28)
    except IOError as e:
        print(e)


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


def get_radio(text, i):
    client = AipSpeech(config.APP_ID, config.API_KEY, config.SECRET_KEY)
    result = client.synthesis(text, 'zh', 1, {
        'spd': 3,
        'vol': 10,
        'pit': 6,
        'per': 4
    })
    if not isinstance(result, dict):
        with open('auido_%s.mp3' % str(i), 'wb') as f:
            f.write(result)


def get_radio_2(text, i):
    url = config.KD_RADIO_URL
    r = requests.post(url, headers=getHeader(), data={"text": text})

    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        sid = r.headers['sid']
        if config.AUE == "raw":
            print(r.content)
            #   合成音频格式为pcm、wav并保存在audio目录下
            writeFile("" + sid + ".wav", r.content)
        else:
            print(r.content)
            #   合成音频格式为mp3并保存在audio目录下
            writeFile("auido_" + str(i) + ".mp3", r.content)
        print("success, sid = " + sid)
    else:
        #   错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
        print(r.text)


def getHeader():
    curTime = str(int(time.time()))
    # ttp=ssml
    param = "{\"aue\":\"" + config.AUE + "\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\",\"volume\":\"60\",\"pitch\":\"20\"}"
    # print("param:{}".format(param))

    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    # print("x_param:{}".format(paramBase64))

    m2 = hashlib.md5()
    m2.update((config.API_KEY + curTime + paramBase64).encode('utf-8'))

    checkSum = m2.hexdigest()
    print('checkSum:{}'.format(checkSum))

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': config.APPID,
        'X-CheckSum': checkSum,
        'X-Real-Ip': '127.0.0.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    print(header)
    return header


def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()
