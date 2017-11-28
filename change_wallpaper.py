# -*- coding: utf-8 -*-
"""
从指定文件夹随机获取一个图片并设置为壁纸。
"""

from datetime import datetime

import config

print("当前时间：%s" % (datetime.now().strftime("%F %T")))

def main():
    image_name, count = config.get_random_image_from_db()
    print("壁纸总数：%d" % (count,))
    config.set_wallpaper(image_name)


if __name__ == "__main__":
    main()
