# -*- coding:utf-8 -*-
import os
from generate_img.generate_img import generate_bg_img
from generate_img.generate_img import generate_img
from generate_img.generate_img import get_text
from generate_img.generate_img import img_to_video
from generate_img.generate_img import video_to_img

if __name__ == '__main__':
    # video_to_img()

    if os.path.exists('bg.png') == False:
        generate_bg_img()
    #
    text_list_all = get_text()
    if len(text_list_all) > 0:
        for text_list in text_list_all:
            i = 1
            for text in text_list:
                generate_img(text, i, 50)
                i += 1
            #  generate_img(text, i, 50, text_list[i])
            img_to_video(len(text_list))
