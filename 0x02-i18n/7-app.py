#!/usr/bin/env python3
'''Task 7 Module'''
from babel.dates import get_timezone_name
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict
import pytz


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
def get_locale() -> str:
    '''determine the best match with languages.'''
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    user_locale = request.args.get('login_as')
    if user_locale:
        usr_local = users.get(int(user_locale)).get('locale')
        if usr_local in app.config['LANGUAGES']:
            return usr_local

    headers = request.headers.get("locale", '')
    if headers in app.config["LANGUAGES"]:
        return headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def validate_timezone(timezone):
    '''validates the timezone'''
    try:
        pytz.timezone(timezone)  # Validate the time zone
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.timezoneselector
def get_timezone():
    '''get the user's preferred time zone'''
    url_timezone = request.args.get('timezone')
    if url_timezone:
        return validate_timezone(url_timezone)

    if hasattr(g, 'user') and 'timezone' in g.user:
        return validate_timezone(g.user['timezone'])

    return 'UTC'


@app.route('/')
def index():
    '''index route'''
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
