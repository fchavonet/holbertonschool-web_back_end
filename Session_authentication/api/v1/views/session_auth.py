#!/usr/bin/env python3
"""
Session authentication view.
"""

import os
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def session_auth_login():
    """
    Handles session authentication login.
    """
    from api.v1.app import auth

    # Retrieve email and password from request form.
    email = request.form.get("email")
    password = request.form.get("password")

    # Validate email.
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Validate password.
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Search for a user with the provided email.
    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Validate the provided password.
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session ID for the authenticated user.
    session_id = auth.create_session(user.id)

    # Prepare the response with user details (excluding sensitive data).
    response = jsonify(user.to_json())

    # Retrieve session cookie name from environment variables.
    session_name = os.getenv("SESSION_NAME")
    if session_name:
        response.set_cookie(session_name, session_id)

    return response


@app_views.route(
    "/auth_session/logout",
    methods=["DELETE"],
    strict_slashes=False
)
def session_auth_logout():
    """
    Handles session logout.
    """
    from api.v1.app import auth

    # Attempt to destroy the session; return 404 if it fails.
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
