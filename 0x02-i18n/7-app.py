#!/usr/bin/env python3
"""
A Basic Flask app module
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config():
    """this Represents a flask babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """This Retrieves a user based on a user id"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """This performs some routines before each request """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """function that gets the locale for a web page"""
    locale = request.args.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config['LANGUAGES']:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """function that retrieves the timezone for a web page"""
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/")
def index():
    """index view"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
