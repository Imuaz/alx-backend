#!/usr/bin/env python3
'''Task 5 Module'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


app = Flask(__name__)


class Config:
    '''set Babel’s default locale and timezone'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''get user by ID or return None'''
    user = request.args.get('login_as')
    if user:
        return users.get(int(user))
    return None

@app.before_request
def before_request() -> None:
    '''executes before all other functions.'''
    user = get_user()
    if user:
        g.user = user

@babel.localeselector
def get_locale():
    '''determine the best match with languages.'''
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''1-index home page'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
