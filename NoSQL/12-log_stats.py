#!/usr/bin/env python3
""" Module that provides some stats about Nginx logs stored in MongoDB. """

from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.count_documents({})} logs\nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    logs_dict = {}

    for method in methods:
        logs_dict[method] = nginx_collection.count_documents(
            {"method": method}
        )

    for method, logs in logs_dict.items():
        print(f"\tmethod {method}: {logs}")

    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_checks} status check")
