# -*- coding: utf-8 -*-

import argparse
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=1027)
    parser.add_argument("--host", type=str, default="127.0.0.1")
    args = parser.parse_args()
    app.run(port=args.port, host=args.host)
