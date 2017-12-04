# -*- coding: utf-8 -*-
"""
从指定文件夹随机获取一个图片并设置为壁纸。
"""

import os
import sys
import glob
import ctypes
import random
import sqlite3
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

def get_image_list():
    image_list = glob.glob(wallpaper_path + r"\**\*jpg", recursive=True)
    return image_list


def get_image_size(file):
    im = Image.open(file)
    return im.size[0]


def create_or_open_db():
    # path_name = os.path.dirname(sys.argv[0])
    path_name = wallpaper_path
    db_file = os.path.join(path_name, "wallpapers.db")
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    if db_is_new:
        logging.info("Creating db %s" % (db_file,))
        sql = '''CREATE TABLE IF NOT EXISTS wallpaper(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    wallpaper TEXT,
                    status INTEGER NOT NULL DEFAULT 0);'''
        c.execute(sql)
        logging.info("Init db %s" % (db_file,))
        image_list = get_image_list()
        for image_file in image_list:
            image_size = get_image_size(image_file)
            if image_size >= 1920:
                sql = '''INSERT INTO wallpaper
                    (wallpaper)
                    VALUES(?);'''
                c.execute(sql, [image_file])
        conn.commit()
    else:
        pass
    return conn, c



def insert_db(image_file):
    conn, c = create_or_open_db()
    sql = '''INSERT INTO wallpaper
                (wallpaper)
                VALUES(?);'''
    c.execute(sql, [image_file])
    conn.commit()


def get_random_image_from_db():
    conn, c = create_or_open_db()
    c.execute("SELECT max(id) FROM wallpaper")
    max_id = list(c.fetchone())[0]
    key = random.randint(1, max_id)
    num = (key,)
    c.execute("SELECT wallpaper FROM  wallpaper WHERE id = ?", num)
    ret = c.fetchone()
    image_name = list(ret)[0]
    conn.close()
    return image_name, max_id


def get_latest_image_from_db():
    conn, c = create_or_open_db()
    c.execute("SELECT max(id) FROM wallpaper")
    max_id = list(c.fetchone())[0]
    num = (max_id,)
    c.execute("SELECT wallpaper FROM  wallpaper WHERE id = ?", num)
    ret = c.fetchone()
    image_name = list(ret)[0]
    conn.close()
    return image_name, max_id


def set_wallpaper(image):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, 3)
    logging.info("当前壁纸: %s" % (image,))


def main():
    pass


user_home = os.environ.get("USERPROFILE")
wallpaper_path = user_home + r"\Pictures\Wallpaper"
bing_path = user_home + r"\Pictures\Wallpaper\Bing"
bingcom_path = user_home + r"\Pictures\Wallpaper\Bingcom"
pc_path = user_home + r"\Pictures\Wallpaper\Spotlight\PC"
theme_path = user_home + r"\Pictures\Wallpaper\Theme"

if __name__ == "__main__":
    main()
