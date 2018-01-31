# -*- coding: utf-8 -*-
"""
从指定文件夹随机获取一个图片并设置为壁纸。
"""

import config


def main():
    image_name, count = config.get_random_image_from_db()
    config.set_wallpaper(image_name)


if __name__ == "__main__":
    main()
