#!/usr/bin/env python3
'''Task 6 Module'''
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


def get_user():
    '''get user by ID or return None'''
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    '''executes before all other functions.'''
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """select the best match for supported languages"""
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        print(f"locale {locale}")
        return locale
    user_locale = g.user.get('locale')
    if user_locale in app.config['LANGUAGES']:
        print(f"user_locale {user_locale}")
        return user_locale
    b_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if b_locale in app.config['LANGUAGES']:
        print(f"browser_locale {b_locale}")
        return b_locale
    return "en"


@app.route('/')
def index():
    '''index route'''
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
