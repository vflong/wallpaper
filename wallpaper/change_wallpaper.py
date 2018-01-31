# -*- coding: utf-8 -*-
"""
从指定文件夹随机获取一个图片并设置为壁纸。
"""

from config import get_random_image_from_db, set_wallpaper


def main():
    image_name, count = get_random_image_from_db()
    set_wallpaper(image_name)


if __name__ == "__main__":
    main()
