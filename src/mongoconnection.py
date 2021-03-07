from pymongo import MongoClient

client = MongoClient()
db = client.mad_green

def read_coll(collection,query, client=client):
    res = db[collection].find(query)
    return list(res)

def write_coll(collection, obj,client=client):
    res = db[collection].insert_one(obj)
    return res