#!/usr/bin/env python3
""" Module that lists all documents in a collection. """


def list_all(mongo_collection):
    """
    Retrieve all documents from the specified MongoDB collection.

    Parameters:
    - mongo_collection: the MongoDB collection to retrieve documents from.

    Returns:
    A cursor object containing all documents in the collection.
    """
    return mongo_collection.find()
