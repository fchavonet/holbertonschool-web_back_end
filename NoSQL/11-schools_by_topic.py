#!/usr/bin/env python3
""" Module that returns the list of school having a specific topic. """


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools from the specified
    MongoDB collection that have a specific topic.

    Parameters:
    - mongo_collection: the MongoDB collection to search for schools.
    - topic: the specific topic to filter schools by.

    Returns:
    A cursor object containing the schools with the specified topic.
    """
    return mongo_collection.find({"topics": topic})
