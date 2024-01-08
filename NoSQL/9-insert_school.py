#!/usr/bin/env python3
""" Module that inserts a new document in a collection based on `kwargs`. """


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the specified MongoDB collection.

    Parameters:
    - mongo_collection: the MongoDB collection to insert the document into.
    - **kwargs: keyword arguments representing the fields
                and values of the new document.

    Returns:
    The ObjectId of the newly inserted document.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
