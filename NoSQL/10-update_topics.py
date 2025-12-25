#!/usr/bin/env python3
"""
Module 10-update_topics
Contains function update_topics to update topics of a document
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name: The name of the school to update (string).
        topics: The list of topics (list of strings).
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
