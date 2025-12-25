#!/usr/bin/env python3
"""
Module 8-all
Contains function list_all to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of documents (dictionaries).
        Returns an empty list if no documents are found.
    """
    # .find() returns a cursor; list() converts it to a list of dicts
    return list(mongo_collection.find())
