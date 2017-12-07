# -*- coding: utf-8 -*-

import os
import shutil
import logging

import config
import utils

"""
Windows 10 only.
Get Spotlight Picture.
"""

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

print("\n### 获取 Windows 10 聚焦锁屏结果 ###")


def get_src_file():
    os.chdir(src_path)
    count = 0
    for file in os.listdir('.'):
        if os.stat(file).st_size / 1024 > 100:
            imsize = config.get_image_size(file)
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
            print(dst)
            count = count + 1
    return count


def main():
    status = get_src_file()
    utils.get_image_action(status)


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

