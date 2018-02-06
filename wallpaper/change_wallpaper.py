# -*- coding: utf-8 -*-
"""
从指定文件夹随机获取一个图片并设置为壁纸。
"""

from config import get_random_image_from_db, set_wallpaper


def main():
    image_name, image_id = get_random_image_from_db()
    set_wallpaper(image_name)
    return image_name, image_id


if __name__ == "__main__":
    main()
