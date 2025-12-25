#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Contains function schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: The topic searched (string).

    Returns:
        A list of dictionaries (documents) matching the topic.
    """
    # MongoDB automatically searches inside the array for the value
    return list(mongo_collection.find({"topics": topic}))
