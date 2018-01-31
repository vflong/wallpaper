# -*- coding: utf-8 -*-

"""
Windows 10 only.
Get Spotlight Picture.
"""

from utils import get_spotlight_src_file
from utils import get_image_action


def main():
    status = get_spotlight_src_file()
    get_image_action(status)


if __name__ == "__main__":
    main()

