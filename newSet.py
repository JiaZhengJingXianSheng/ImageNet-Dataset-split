# This is to fix the peer label to set data
# Arthur: Liu Yu Zhao
# Time: 2021/7/12 21:12
# This is a new program for divide imageNet dataset 
import os
from shutil import copy, rmtree
import random


def mk_file(file_path: str):
    if os.path.exists(file_path):
        # If folder exist , delete this folder then new a folder
        rmtree(file_path)
    os.makedirs(file_path)


origin_path = './train/train'
image_class = [cla for cla in os.listdir(origin_path)
               if os.path.isdir(os.path.join(origin_path, cla))]

mk_file('newTrain')
mk_file('newVal')

val_root = './newVal'
train_root = './newTrain'
for cla in image_class:
    # new folder
    mk_file(os.path.join(val_root, cla))
    mk_file(os.path.join(train_root,cla))

image_class_num = len(image_class)
i = 0


for cla in image_class:
    cla_path = os.path.join(origin_path, cla)
    images = os.listdir(cla_path)
    num = len(images)
    i = i + 1
    # seed index
    # copy 5 image as val data
    eval_index = random.sample(images, k=int(5))
    for index, image in enumerate(images):
        if image in eval_index:
            image_path = os.path.join(cla_path, image)
            new_path = os.path.join(val_root, cla)
            copy(image_path, new_path)

        else:
            train_image_path = os.path.join(cla_path,image)
            new_train_path = os.path.join(train_root,cla)
            copy(train_image_path ,new_train_path)
    print("\rVal data setting\tAll processing [{}/{}]".format(i, image_class_num), end="")  # processing bar

print("\nVal data processes done!")
