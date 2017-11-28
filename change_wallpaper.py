# -*- coding: utf-8 -*-
"""
从指定文件夹随机获取一个图片并设置为壁纸。
"""

import logging
import config

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%a, %d %b %Y %H:%M:%S")

def main():
    image_name, count = config.get_random_image_from_db()
    logging.info("壁纸总数：%d" % (count,))
    config.set_wallpaper(image_name)


if __name__ == "__main__":
    main()
