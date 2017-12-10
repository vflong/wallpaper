# -*- coding: utf-8 -*-

import utils


def main():
    status = utils.get_bing_src_file()
    utils.get_image_action(status)


if __name__ == "__main__":
    main()
