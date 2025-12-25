#!/usr/bin/env python3
"""
Module 12-log_stats
Reads logs from MongoDB and prints stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to default local instance
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Count by method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Count status check (method=GET and path=/status)
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
