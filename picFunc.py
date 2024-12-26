# -*- coding:utf-8 -*-
# @FileName  :picFunc.py
# @Time      :2024/12/25 11:38
# @Author    :Ray
from PIL import Image, ImageOps

def border_image(image, border_widths=(10, 10, 10, 100), border_color=(255,255,255)):
    image_with_border = ImageOps.expand(image, border=border_widths, fill=border_color)
    return image_with_border

def merge_pic_horizontal(image1, image2):
    # 获取图片大小
    width1, height1 = image1.size
    width2, height2 = image2.size


    #创建空白图片
    new_image = Image.new("RGB", (width1 + width2, height1), (255, 255, 255))



def merge_pic_vertical(image1, image2):
    # 获取图片大小
    width1, height1 = image1.size
    width2, height2 = image2.size

    #创建空白图片