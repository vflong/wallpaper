# -*- coding: utf-8 -*-

import os
import sys
import json
import shutil
import logging
import platform
import requests
import xml.etree.ElementTree

from config import *
from path import wallpaper_path, src_path, bing_path, bingcom_path, spotlight_path, pc_path, tablet_path, theme_path

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

# if not platform.platform().startswith("Windows-10"):
#     sys.exit("Windows 10 only.")


def get_image_action(count):
    if count == 0:
        logging.info("404 Not found")
        print("### 未发现新壁纸，壁纸未更新 ###")
    else:
        logging.info("Congratulation! You have get " + str(count) + " images.")
        image, image_id = get_latest_image_from_db()
        print("\n### 更新壁纸 ###")
        print("New wallpaper: \n%d %s" % (image_id, image,))
        set_wallpaper(image)


def get_spotlight_src_file():
    os.chdir(src_path)
    count = 0
    for file in os.listdir('.'):
        if os.stat(file).st_size / 1024 > 100:
            imsize = get_image_size(file)
            if imsize == 1920:
                dst = pc_path + "\\" + file + ".jpg"
                if not os.path.exists(dst):
                    shutil.copy2(file, dst)
                    insert_db(dst)
                    count = count + 1
            elif imsize == 1080:
                dst = tablet_path + "\\" + file + ".jpg"
                shutil.copy2(file, dst)
            else:
                continue

            if os.path.exists(dst):
                continue
            print(dst)
    return count


def get_bing_src_file():
    os.chdir(bing_path)
    count = 0
    for i in range(8):
        url = "http://az517271.vo.msecnd.net/TodayImageService.svc/HPImageArchive?mkt=zh-cn&idx=" + str(i)
        r = requests.get(url)
        if r.status_code == 200:
            with open("temp.xml", "w", encoding="utf-8") as f:
                f.write(str(r.text))
            e = xml.etree.ElementTree.parse('temp.xml').getroot()
            os.remove('temp.xml')
            image_url = e[6].text
            logging.info("图片网址：%s" % (image_url,))
            image_name = image_url.split('/')[-1]
            if not os.path.exists(image_name):
                image_data = requests.get(image_url, stream=True)
                with open(image_name, 'wb') as f:
                    shutil.copyfileobj(image_data.raw, f)
                del image_data
                count = count + 1
                image_file = os.path.join(bing_path, image_name,)
                insert_db(image_file)
                logging.info("Image list: %s\n" % (image_name,))
            else:
                continue
        else:
            pass
    return count


def get_bingcom_src_file():
    os.chdir(bingcom_path)
    count = 0
    for i in range(8):
        url_prefix = "https://www.bing.com"
        url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx={0}&n=1&mkt=en-US".format(i)
        r = requests.get(url)
        if r.status_code == 200:
            jsfile = json.loads(r.text)
            url_suffix = jsfile["images"][0]["url"]
            image_url = url_prefix + url_suffix
            logging.info("图片网址：%s" % (image_url,))
            image_name = image_url.split('/')[-1]
            if not os.path.exists(image_name):
                image_data = requests.get(image_url, stream=True)
                with open(image_name, 'wb') as f:
                    shutil.copyfileobj(image_data.raw, f)
                del image_data
                count = count + 1
                image_file = os.path.join(bingcom_path, image_name,)
                insert_db(image_file)
                logging.info("Image list: %s\n" % (image_name,))
            else:
                continue
        else:
            pass
    return count


if __name__ == "__main__":
    pass
    # get_image_action()

