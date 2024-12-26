# -*- coding:utf-8 -*-
# @FileName  :fontFunc.py
# @Time      :2024/12/25 11:39
# @Author    :Ray
from PIL import Image, ImageDraw, ImageFont

def draw_font(image, text, position):
    # 在图片上绘制文字
    draw = ImageDraw.Draw(image)
    # 设置字体，字号
    font = ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc", size=75)
    text_color = (0, 0, 0)

    # 绘制文字
    draw.text(position, text, fill=text_color, font=font)
    return image