# -*- coding: utf-8 -*-

import os
import sys
import logging
import platform

import config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

if not platform.platform().startswith("Windows-10"):
    sys.exit("Windows 10 only.")


def get_image_action(count):
    if count == 0:
        logging.info("404 Not found")
        print("### 未发现新壁纸，壁纸未更新 ###")
    else:
        logging.info("Congratulation! You have get " + str(count) + " images.")
        image, image_id = config.get_latest_image_from_db()
        print("\n### 更新壁纸 ###")
        print("New wallpaper: \n%d %s" % (image_id, image,))
        config.set_wallpaper(image)


user_home = os.environ.get("USERPROFILE")
src_path = user_home + r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
spotlight_path = user_home + r"\Pictures\Wallpaper\Spotlight"
pc_path = spotlight_path + r"\PC"
table_path = spotlight_path + r"\Tablet"
theme_path = user_home + r"\Pictures\Wallpaper"
bing_path = user_home + r"\Pictures\Wallpaper\Bing"

os.makedirs(spotlight_path, exist_ok=True)
os.makedirs(pc_path, exist_ok=True)
os.makedirs(table_path, exist_ok=True)
os.makedirs(theme_path, exist_ok=True)
os.makedirs(bing_path, exist_ok=True)


if __name__ == "__main__":
    get_image_action()

