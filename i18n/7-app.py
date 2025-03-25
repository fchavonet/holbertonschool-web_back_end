#!/usr/bin/env python3

"""
Basic Flask application with a single route.
"""

import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """
    Configuration class for the Flask app.

    Attributes:
        LANGUAGES: List of supported languages.
        BABEL_DEFAULT_LOCALE: Default language.
        BABEL_DEFAULT_TIMEZONE: Default timezone.
    """

    LANGUAGES = ["en", "fr"]
    # BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    """
    # Selects the best matching language from the request headers.

    Priority:
    1. Locale from URL parameters.
    2. User's preferred locale (if any).
    3. Accept-Language headers.
    4. Default locale.

    Returns:
        A language code ("en" or "fr").
    """

    # 1. URL parameter
    locale = request.args.get("locale")

    if locale in app.config["LANGUAGES"]:
        return locale

    # 2. User preference
    if g.get("user"):
        user_locale = g.user.get("locale")

        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    # 3. Request headers
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    Gets a user from the login_as URL parameter.

    Returns:
        A user dictionary if found, otherwise None.
    """

    try:
        user_id = int(request.args.get("login_as", 0))
        return users.get(user_id)
    except Exception:
        return None


def get_timezone():
    """
    Determines the best timezone to use for the request.

    Priority:
    1. Timezone from URL parameters (if valid).
    2. Timezone from user settings (if valid).
    3. Default: UTC.
    """

    tz_param = request.args.get("timezone")

    if tz_param:
        try:
            return str(pytz.timezone(tz_param))
        except UnknownTimeZoneError:
            pass

    if g.get("user"):
        user_tz = g.user.get("timezone")

        if user_tz:
            try:
                return str(pytz.timezone(user_tz))
            except UnknownTimeZoneError:
                pass

    return "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """
    Executed before each request to set g.user if logged in.
    """

    g.user = get_user()


@app.route("/")
def index():
    """
    Renders the index page.

    Returns:
         Rendered HTML template.
    """

    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
