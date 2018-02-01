# -*- coding: utf-8 -*-
"""
从指定文件夹随机获取一个图片并设置为壁纸。
"""

import os
import glob
import hashlib
import ctypes
import random
import sqlite3
import logging
from PIL import Image
from datetime import datetime

from path import wallpaper_path, src_path, bing_path, bingcom_path, spotlight_path, pc_path, tablet_path, theme_path

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

def get_image_list():
    image_list = glob.glob(wallpaper_path + r"\**\*jpg", recursive=True)
    return image_list


def get_image_size(file):
    im = Image.open(file)
    return im.size[0]


def get_image_sha256(file):
    sha256 = hashlib.sha256(open(file, 'rb').read()).hexdigest()
    return sha256


def get_image_ctime(file):
    raw_time = os.path.getctime(file)
    ctime = datetime.fromtimestamp(raw_time).strftime("%F %T")
    return ctime

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
                    dirname TEXT,
                    basename TEXT,
                    sha256 TEXT,
                    timestamp DATETIME DEFAULT (datetime('now', 'localtime')),
                    status INTEGER NOT NULL DEFAULT 0);'''
        c.execute(sql)
        logging.info("Init db %s" % (db_file,))
        image_list = get_image_list()
        for image_file in image_list:
            image_size = get_image_size(image_file)
            if image_size >= 1920:
                sha256 = get_image_sha256(image_file)
                ctime = get_image_ctime(image_file)
                dirname, basename = (os.path.dirname(image_file), os.path.basename(image_file))
                sql = '''INSERT INTO wallpaper
                    (wallpaper, dirname, basename, sha256, timestamp)
                    VALUES(?, ?, ?, ?, ?);'''
                c.execute(sql, [image_file, dirname, basename, sha256, ctime])
    else:
        pass
    return conn, c



def insert_db(image_file):
    conn, c = create_or_open_db()
    sha256 = get_image_sha256(image_file)
    ctime = get_image_ctime(image_file)
    dirname, basename = (os.path.dirname(image_file), os.path.basename(image_file))
    sql = '''INSERT INTO wallpaper
                    (wallpaper, dirname, basename, sha256, timestamp)
                    VALUES(?, ?, ?, ?, ?);'''
    c.execute(sql, [image_file, dirname, basename, sha256, ctime])
    conn.commit()
    conn.close()


def get_random_image_from_db():
    conn, c = create_or_open_db()
    c.execute("SELECT max(id) FROM wallpaper")
    max_id = list(c.fetchone())[0]
    key = random.randint(1, max_id)
    num = (key,)
    c.execute("SELECT wallpaper FROM  wallpaper WHERE id = ?", num)
    ret = c.fetchone()
    image_name = list(ret)[0]
    c.execute("UPDATE wallpaper SET status  = 0 WHERE status  = 1;")
    c.execute("UPDATE wallpaper SET status  = 1 WHERE wallpaper = ?;", (image_name,))
    conn.commit()
    conn.close()
    logging.info("壁纸总数：%d" % (max_id,))
    return image_name, max_id


def get_latest_image_from_db():
    conn, c = create_or_open_db()
    c.execute("SELECT max(id) FROM wallpaper")
    max_id = list(c.fetchone())[0]
    num = (max_id,)
    c.execute("SELECT wallpaper FROM  wallpaper WHERE id = ?", num)
    ret = c.fetchone()
    image_name = list(ret)[0]
    c.execute("UPDATE wallpaper SET status  = 0 WHERE status  = 1;")
    c.execute("UPDATE wallpaper SET status  = 1 WHERE wallpaper = ?;", (image_name,))
    conn.commit()
    conn.close()
    logging.info("壁纸总数：%d" % (max_id,))
    return image_name, max_id


def get_all_image_from_db():
    conn, c = create_or_open_db()
    c.execute("SELECT * FROM  wallpaper;")
    ret = c.fetchall()
    image_list = list(ret)
    conn.commit()
    conn.close()
    return image_list


def get_one_image_from_db(id):
    conn, c = create_or_open_db()
    c.execute("SELECT max(id) FROM wallpaper")
    max_id = list(c.fetchone())[0]
    if int(id) > max_id:
        id = max_id
    num = (int(id),)
    c.execute("SELECT * FROM  wallpaper WHERE id = ?", num)
    ret = c.fetchall()
    image_name = list(ret)
    conn.commit()
    conn.close()
    return image_name


def set_wallpaper(image):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, 3)
    logging.info("当前壁纸: %s" % (image,))



