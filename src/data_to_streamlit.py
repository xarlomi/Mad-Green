from pymongo import MongoClient
# mi .py mongoconnection no se importa! wtf: funcion read_coll y check_exists son de ahi

client = MongoClient()
db = client.mad_green
import pandas as pd


def carga_data():
    data = pd.read_csv("data/cbd_info2.csv")
    return data

def read_coll(collection,query,project, client=client):
    res = db[collection].find(query,  project)
    return list(res)

def check_exists(query, collection, *pro):
    res = read_coll(collection, query, pro)
    if len(res) > 0:
        return True
    else:
        return False

#Returns a list with all the moods that CBD makes you feel
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


#This counts how many kind of CBDs exist that will make you feel in function of the choosen moood 
def count_cbd_mood(mood):
    moods = db.cbd_info.count({"mood": {"$regex": f"{mood}"}})
    return moods

#This function returns a bud shop in function of the mood desired to feel by user:
def shop_mood(moods):
    filt = {"mood":{"$regex":f"{moods}"}}
    project = {"_id":0, "product":1}
    result = db.cbd_info.find(filt, project)
    results= list(result)
    
    lista_res = []
    for i in results:
        q = {"product":i["product"]}
        pro = {"_id":0} 
        if check_exists(q, "cbd_shops"):
            lista_res.append(read_coll("cbd_shops",q,  pro))
            flat_list = [item for sublist in lista_res for item in sublist]
            df = pd.DataFrame(flat_list)
    return df.sort_values(['price'], ascending=[False])

