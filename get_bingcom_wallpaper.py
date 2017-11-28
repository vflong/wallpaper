# -*- coding: utf-8 -*-

import os
import sys
import json
import shutil
import logging
import requests

import config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

def get_image():
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
                image_newest = image_file
                config.insert_db(image_file)
                logging.info("Image list: %s\n" % (image_name,))
            else:
                continue
        else:
            pass
    if count == 0:
        print("### 没有获取到新图片 ###")
        sys.exit(404)
    else:
        return image_newest


def main():
    os.makedirs(bingcom_path, exist_ok=True)
    os.chdir(bingcom_path)
    image_file = get_image()
    config.set_wallpaper(image_file)


user_home = os.environ.get("USERPROFILE")
bingcom_path = user_home + r"\Pictures\Wallpaper\Bingcom"


if __name__ == "__main__":
    main()
