#!/usr/bin/env python3

"""
Module for the basic Flask app for the user authentication service.
"""

from auth import Auth
from flask import Flask, jsonify, Response

app = Flask(__name__)
auth = Auth()


@app.route("/", methods=["GET"])
def home() -> Response:
    """
    GET route that returns a JSON payload with a welcome message.

    Returns:
        Response: JSON response with the message "Bienvenue".
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
