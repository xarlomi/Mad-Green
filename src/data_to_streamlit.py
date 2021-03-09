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


def mood_list():
    """
    Returns a list with all the moods that CBD makes you feel (col1)
    """
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
    """
    Esta funcion cuenta numero de tipos de CBD que te hacen sentir el mood que hayas elegido (col1, q1)
    """
    moods = db.cbd_info.count({"mood": {"$regex": f"{mood}"}})
    return moods



def shop_mood(moods):
    """
    Esta funcion devuelve los productos que puede comprar el usuario (col2, q2) en funcion del mood que haya elegido (col1, q1)
    """
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
            
    return flat_list


def shop_rating(moods):
    """
    Esta funcion toma la funcion de arriba Y: me de los ratings (col3, q3) de los productos que puede comprar el usuario (col2, q2) en funcion del mood que haya elegido (col1, q1)
    """
    flat_list = shop_mood(moods)
    lista_ratings = []
    for ratings in flat_list:
            qu= {"product":ratings["product"]}
            pro = {"_id":0}
            if check_exists(qu, "cbd_ratings"):
                    lista_ratings.append( read_coll("cbd_ratings",qu, pro))
                    flat_list2 = [item for sublist in lista_ratings for item in sublist]
                    ratings_df = pd.DataFrame(flat_list2)
                    rate_df = ratings_df.drop_duplicates(subset="product")

    return rate_df

