#!/usr/bin/env python3

"""
Module for the basic Flask app for the user authentication service.
"""

from auth import Auth
from flask import Flask, jsonify, request, Response

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
