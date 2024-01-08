#!/usr/bin/env python3
""" Module that changes all topics of a school document based on the name. """


def update_topics(mongo_collection, name, topics):
    """
    Update topics in documents of the specified MongoDB collection.

    Parameters:
    - mongo_collection: the MongoDB collection containing documents to update.
    - name: the name identifying the documents to be updated.
    - topics: the new topics to set for the specified documents.

    Returns:
    None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
