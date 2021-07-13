# This is to fix the peer label to set data
# Arthur: Liu Yu Zhao
# Time: 2021/7/11 02:31 AM

import os
from shutil import copy, rmtree


def mk_file(file_path: str):
    if os.path.exists(file_path):
        # If folder exist , delete this folder then new a folder
        rmtree(file_path)
    os.makedirs(file_path)


f = open("label.txt", "r")
lines = f.readlines()
origin_label = []

for line in lines:
    str_list = line.split(' ')[0]
    l = line.split(' ')[1].split('\n')[0].split(',')[0]
    origin_label = origin_label + [[str_list, l]]

origin_path = 'C:\\Users\\The_U\\Desktop\\PytorchLearning\\VGG\\sketch'

image_class = [cla for cla in os.listdir(origin_path)
               if os.path.isdir(os.path.join(origin_path, cla))]

mk_file('train')

for cla in image_class:
    # new folder
    for i in origin_label:
        if cla == i[0]:
            mk_file(os.path.join('train', i[1]))

train_path = 'C:\\Users\\The_U\\Desktop\\VGG_Data\\train'

image_class_num = len(image_class)
i = 0
for cla in image_class:
    cla_path = os.path.join(origin_path, cla)
    images = os.listdir(cla_path)
    num = len(images)

    i = i + 1
    for index, image in enumerate(images):
        train_image_path = os.path.join(cla_path, image)
        for x, y in origin_label:
            if x == cla:
                train_new_path = os.path.join(train_path, y)
                copy(train_image_path, train_new_path)
    print("\rTrain data setting\t{}\tAll processing [{}/{}]".format(cla, i, image_class_num),
          end="")
print('\nTrain data processes done!')
