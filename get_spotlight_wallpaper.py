# -*- coding: utf-8 -*-

import os
import sys
import shutil
import logging
import platform
from PIL import Image
from datetime import datetime

import config

"""
Windows 10 only.
Get Spotlight Picture.
"""

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

print("\n### 获取 Windows 10 聚焦锁屏结果 ###")

if not platform.platform().startswith("Windows-10"):
    sys.exit("Windows 10 only.")


def get_image_info(file):
    im = Image.open(file)
    print(file, im.size, im.mode)


def get_image_size(file):
    im = Image.open(file)
    return im.size[0]


def get_src_file():
    os.chdir(src_path)
    count = 0
    for file in os.listdir('.'):
        if os.stat(file).st_size / 1024 > 100:
            imsize = get_image_size(file)
            if imsize == 1920:
                dst = pc_path + "\\" + file + ".jpg"
                if not os.path.exists(dst):
                    config.insert_db(dst)
            elif imsize == 1080:
                dst = table_path + "\\" + file + ".jpg"
            else:
                continue

            if os.path.exists(dst):
                continue
            shutil.copy2(file, dst)
            get_image_info(dst)
            count = count + 1

    if count == 0:
        logging.info("404 Not found")
        return 404
    else:
        logging.info("Congratulation! You have get " + str(count) + " images.")
        return 200


def list_current_dir_image_info(path):
    print("\n### Directory:  " + path + " ###\n")
    os.chdir(path)
    for i, file in enumerate(os.listdir('.')):
        get_image_info(file)
    file_total = i + 1
    print("Total: " + str(file_total))


def get_all_images_info(*args):
    for path in args:
        list_current_dir_image_info(path)


def main():
    status = get_src_file()
    if status == 200:
        image, image_id = config.get_latest_image_from_db()
        print("\n### 更新壁纸 ###")
        print("New wallpaper: \n%d %s" % (image_id, image,))
        config.set_wallpaper(image)
    else:
        print("### 未发现新壁纸，壁纸未更新 ###")


user_home = os.environ.get("USERPROFILE")
src_path = user_home + r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
spotlight_path = user_home + r"\Pictures\Wallpaper\Spotlight"
pc_path = spotlight_path + r"\PC"
table_path = spotlight_path + r"\Tablet"
theme_path = user_home + r"\Pictures\Wallpaper"

os.makedirs(spotlight_path, exist_ok=True)
os.makedirs(pc_path, exist_ok=True)
os.makedirs(table_path, exist_ok=True)
os.makedirs(theme_path, exist_ok=True)


if __name__ == "__main__":
    main()

# get_all_images_info(pc_path, table_path)

