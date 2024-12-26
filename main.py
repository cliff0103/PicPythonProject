# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2024/12/25 11:03
# @Author    :Ray
from idlelib.outwin import file_line_pats
from fileFunc import save_image
from picFunc import border_image
from PIL import Image
from fontFunc import draw_font
import os
pic_path = r"C:\Users\user-f824\Desktop\新建文件夹\地下停车场收费指南岗亭"

for file in os.listdir(pic_path):
    file_path = os.path.join(pic_path, file)
    file_name = file.split('.')[0]
    if os.path.isfile(file_path):
        print(file_path)
        image = Image.open(file_path)
        image = border_image(image)
        width, height = image.size
        position = (int(width/2), height-75)
        image = draw_font(image, file_name, position)
        new_file = os.path.join(pic_path, 'new'+file)
        save_image(image, new_file)
        # image.show()