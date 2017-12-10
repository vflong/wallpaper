# -*- coding: utf-8 -*-

import utils

"""
Windows 10 only.
Get Spotlight Picture.
"""

def main():
    status = utils.get_spotlight_src_file()
    utils.get_image_action(status)


if __name__ == "__main__":
    main()

