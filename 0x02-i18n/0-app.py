#!/usr/bin/env python3
'''basic Flask app Module'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    '''index home page'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500, debug=True)