# -*- coding: utf-8 -*-

import os
import configparser

user_home = os.environ.get("USERPROFILE")
config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_file)

wallpaper_path = os.path.join(user_home, config['Paths']['wallpaper_path'])
src_path = os.path.join(user_home, config['Paths']['src_path'])
bing_path = os.path.join(user_home, config['Paths']['bing_path'])
bingcom_path = os.path.join(user_home, config['Paths']['bingcom_path'])
spotlight_path = os.path.join(user_home, config['Paths']['spotlight_path'])
pc_path = os.path.join(user_home, config['Paths']['pc_path'])
tablet_path = os.path.join(user_home, config['Paths']['tablet_path'])
theme_path = os.path.join(user_home, config['Paths']['theme_path'])


def mkdirs():
    path_list = [wallpaper_path, src_path, bing_path, bingcom_path, spotlight_path, pc_path, tablet_path, theme_path]
    for image_path in path_list:
        os.makedirs(image_path, exist_ok=True)
    return path_list



