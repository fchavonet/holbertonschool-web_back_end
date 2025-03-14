#!/usr/bin/env python3

"""
Module for the basic Flask app for the user authentication service.
"""

from auth import Auth
from flask import Flask
from flask import abort, jsonify, make_response, redirect, request, Response

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def home() -> Response:
    """
    GET route that returns a JSON payload with a welcome message.

    Returns:
        Response: JSON response with the message "Bienvenue".
    """

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> Response:
    """
    POST route that registers a new user.
    Expects form data fields "email" and "password".

    Returns:
        Response: A JSON response containing:
            - On success: the user's email and a message.
            - On failure: a message with a 400 status code.
    """

    email: str = request.form.get("email")
    password: str = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login() -> Response:
    """
    POST route that handles user login.
    Expects form data fields "email" and "password".

    Returns:
        Response: a JSON response containing:
            - On success: the user's email and a login message.
            - On failure: a 401 Unauthorized error.
    """

    email: str = request.form.get("email")
    password: str = request.form.get("password")

    if not email or not password:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id: str = AUTH.create_session(email)

    if not session_id:
        abort(401)

    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id, path="/")

    return response


@app.route("/sessions", methods=["DELETE"])
def logout() -> Response:
    """
    DELETE route that logs out a user.

    Returns:
        A redirect response to the home page,
        or a 403 status code if the session is invalid.
    """

    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
