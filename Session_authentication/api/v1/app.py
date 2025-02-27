#!/usr/bin/env python3
"""
Route module for the API.
"""

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize the authentication instance to None.
auth = None

# Load the appropriate authentication class based on the environment variable.
auth_type = getenv("AUTH_TYPE", None)
if auth_type == "basic_auth":
    auth = BasicAuth()
elif auth_type == "session_auth":
    auth = SessionAuth()
elif auth_type == "auth":
    auth = Auth()


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handles 401 "Unauthorized" errors.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Handles 403 "Forbidden" errors.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handles 404 "Not Found" errors.
    """
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request():
    """
    Handler for processing requests before they reach the route handler.
    """
    if auth is None:
        return

    # Define the list of paths that do not require authentication.
    excluded_paths = ["/api/v1/status/",
                      "/api/v1/unauthorized/",
                      "/api/v1/forbidden/",
                      "/api/v1/auth_session/login/"]

    # Skip authentication if the requested path is excluded.
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Retrieve session ID from the request cookies.
    session_id = auth.session_cookie(request)

    # Abort with a 401 error if the Authorization header is missing.
    if auth.authorization_header(request) is None and session_id is None:
        abort(401)

    # Retrieve the user ID from the session if a session ID is provided.
    user_id = None
    if session_id is not None:
        user_id = auth.user_id_for_session_id(session_id)

    # Set the authenticated user.
    request.current_user = auth.current_user(request)

    # Abort with a 403 error if no valid user is found.
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
