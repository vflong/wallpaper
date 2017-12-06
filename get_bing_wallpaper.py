# -*- coding: utf-8 -*-

import os
import sys
import shutil
import logging
import requests
import xml.etree.ElementTree

import config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

def get_src_file():
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
                config.insert_db(image_file)
                logging.info("Image list: %s\n" % (image_name,))
            else:
                continue
        else:
            pass
    if count == 0:
        logging.info("404 Not found")
        return 404
    else:
        logging.info("Congratulation! You have get " + str(count) + " images.")
        return 200


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
bing_path = user_home + r"\Pictures\Wallpaper\Bing"

os.makedirs(bing_path, exist_ok=True)

if __name__ == "__main__":
    main()
