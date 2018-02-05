# -*- coding: utf-8 -*-

import os
import argparse
from flask import Flask, render_template, make_response

from config import get_random_image_from_db
from config import get_latest_image_from_db
from config import get_all_image_from_db
from config import get_one_image_from_db
from path import wallpaper_path
import change_wallpaper

app = Flask(__name__, static_url_path="", static_folder=wallpaper_path)
app.debug = True


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
    return render_template('image.html', id=id)


@app.route('/random')
def random():
    image_name, image_id = get_random_image_from_db()
    app.static_folder = os.path.dirname(image_name)
    image_url = os.path.basename(image_name)
    return render_template('info.html', image_id=image_id, image_name=image_name, image_url=image_url)


@app.route('/latest')
def latest():
    image_name, image_id = get_latest_image_from_db()
    app.static_folder = os.path.dirname(image_name)
    image_url = os.path.basename(image_name)
    return render_template('info.html', image_id=image_id, image_name=image_name, image_url=image_url)


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
