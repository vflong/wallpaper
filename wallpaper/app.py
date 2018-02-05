# -*- coding: utf-8 -*-

import argparse
from flask import Flask, render_template, make_response

from config import get_random_image_from_db
from config import get_latest_image_from_db
from config import get_all_image_from_db
from config import get_one_image_from_db
import change_wallpaper

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')


@app.route('/all')
def all():
    image_list = get_all_image_from_db()
    with open('templates/wallpaper.1.html', 'w') as f:
        for image in image_list:
            f.write('<tr>' + ' '.join('<td>' + str(item) + '</td>' for item in image) + '</tr>\n')
    return render_template('wallpaper.html')


@app.route('/all/<int:id>')
def one(id):
    image_list = get_one_image_from_db(id)
    with open('templates/image.1.html', 'w') as f:
        for image in image_list:
            f.write('<tr>' + ' '.join('<td>' + str(item) + '</td>' for item in image) + '</tr>\n')
    return render_template('image.html')


@app.route('/random')
def random():
    image_name, max_id = get_random_image_from_db()
    ret = """image_name: {0}
max_id: {1}""".format(image_name, max_id)
    return ret


@app.route('/latest')
def latest():
    image_name, max_id = get_latest_image_from_db()
    ret = """image_name: {0}
max_id: {1}""".format(image_name, max_id)
    return ret


@app.route('/change')
def change():
    image_name = change_wallpaper.main()
    return image_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=1027)
    parser.add_argument("--host", type=str, default="127.0.0.1")
    args = parser.parse_args()
    app.run(port=args.port, host=args.host)
