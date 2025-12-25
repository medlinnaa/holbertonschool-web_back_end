#!/usr/bin/env python3
"""
Module 9-insert_school
Contains function insert_school that inserts a new document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs to be inserted as the document.

    Returns:
        The _id of the newly inserted document.
    """
    # kwargs acts as a dictionary, so we can pass it directly to insert_one
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
