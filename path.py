# -*- coding: utf-8 -*-
"""
define wallpaper path.
"""

import os
import configparser

user_home = os.environ.get("USERPROFILE")
config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_file)


def mkdirs():
    # path_name = ['wallpaper_path', 'src_path', 'bing_path', 'bingcom_path', 'spotlight_path', 'pc_path', 'tablet_path', 'theme_path']
    path_name = list(config['Paths'].keys())
    path_list = []
    for image_path in path_name:
        image_path = os.path.join(user_home, config['Paths'][image_path])
        os.makedirs(image_path, exist_ok=True)
        path_list.append(image_path)
    return path_list

