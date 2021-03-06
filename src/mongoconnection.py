import dns 
from pymongo import MongoClient
from dotenv import load_dotenv
import os


#dburl = os.getenv("dburl")
"""
client = MongoClient(dburl)
db = client.get_database()
"""

#dburl ="mongodb+srv://xarlomi:car99pg611@clustermadgreen.es0ot.mongodb.net/mad_green?retryWrites=true&w=majority"

client = MongoClient()
db = client.mad_green

def read_coll(collection,query,project,  client=client):
    res = db[collection].find(query,  project)
    return list(res)

def write_coll(collection, obj,client=client):
    res = db[collection].insert_one(obj)
    return res

def check_exists(query, collection, *pro):
    res = read_coll(collection, query, pro)
    if len(res) > 0:
        return True
    else:
        return False