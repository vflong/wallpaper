# -*- coding: utf-8 -*-

"""
Get Bing Wallpaper.
"""

from utils import get_bing_src_file
from utils import get_image_action


def main():
    status = get_bing_src_file()
    get_image_action(status)


if __name__ == "__main__":
    main()
