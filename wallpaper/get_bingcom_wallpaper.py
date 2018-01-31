# -*- coding: utf-8 -*-

import utils

"""
Get Bing Picture.
"""


def main():
    status = utils.get_bingcom_src_file()
    utils.get_image_action(status)


if __name__ == "__main__":
    main()
