from pymongo import MongoClient

client = MongoClient()
db = client.mad_green
import pandas as pd


def carga_data():
    data = pd.read_csv("data/cbd_info2.csv")
    return data

def mood_list():
    dat = carga_data()
    a = dat.Effects.unique()
    b = [i.split(",") for i in a]
    z = []
    for j in b:
        for k in j:
            z.append(k)
            z = list(set(z))
            for x in z:
                if x == "None" or x=="Dry" or x=="Mouth":
                    z.remove(x)
    return z
 
def count_cbd_mood(mood):
    moods = db.cbd_info.count({"mood": {"$regex": f"{mood}"}})
    return moods