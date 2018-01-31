# -*- coding: utf-8 -*-

"""
Get Bing Picture.
"""

from utils import get_bingcom_src_file
from utils import get_image_action

def main():
    status = get_bingcom_src_file()
    get_image_action(status)


if __name__ == "__main__":
    main()
