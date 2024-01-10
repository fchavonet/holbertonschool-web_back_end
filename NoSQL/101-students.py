#!/usr/bin/env python3
""" Module that returns all students sorted by average score """


def top_students(mongo_collection):
    """
    Returns a MongoDB aggregation pipeline result
    containing students sorted by average score.

    Args:
        - mongo_collection: the MongoDBcollection containing student data.

    Returns:
        - pymongo.command_cursor.CommandCursor: a cursor with the result of
                                                the aggregation pipeline,
                                                representing students sorted
                                                by average score.
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
