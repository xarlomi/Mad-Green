from pymongo import MongoClient
# mi .py mongoconnection no se importa! wtf: funcion read_coll y check_exists son de ahi
from src.mongoconnection import *

import math
import pandas as pd


def carga_data():
    data = pd.read_csv("data/cbd_info2.csv")
    return data



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


def main_shop_mood(moods):
    """
    This queries one collection to another and returns a DF with the 
    available CBD product given the mood chosen by user. Without website. 
    Main DF used in streamlit
    """
    
   #querying the KAGGLE dataset
    filt = {"mood":{"$regex":f"{moods}"}}
    project = {"_id":0, "product":1}
    result = db.cbd_info.find(filt, project)
    results= list(result)
    
    #querying the SCRAPPED dataset
    lista_res = []
    for i in results:
        q = {"product":i["product"]}
        pro = {"_id":0, "shop":0} 
        if check_exists(q, "cbd_shops"):
            lista_res.append(read_coll("cbd_shops",q,  pro))
            flat_list = [item for sublist in lista_res for item in sublist]
            df = pd.DataFrame(flat_list)

    return df
    
    
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
            flat_lists = [item for sublist in lista_res for item in sublist]
            
    return flat_lists

def mood_description(moods):
    """
    This queries one collection to another and returns a DF with the 
    description of CBD product given the mood chosen by user
    """
    flat_list1 = shop_mood(moods)
    lista_description = []
    for shops in flat_list1:
        qu = {"product":shops["product"]}
        pro = {"_id": 0, "product":1, "description":1}
        if check_exists(qu, "cbd_info"):
                    lista_description.append( read_coll("cbd_info",qu, pro))
                    flat_list2 = [item for sublist in lista_description for item in sublist]
                    df = pd.DataFrame(flat_list2)    

    return df



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
                    rate_df['rating']= round(rate_df['rating'], 2)
                    
    return rate_df


def merging_shop_rating(moods):
    """
    Esta funcion me devuelve un df de df shop_ratings + shoop_moods + cbd description
    """
    df1 = pd.DataFrame(shop_mood(moods))
    df2 = shop_rating(moods)
    df3 = mood_description(moods)
    ttal =  df1.merge(df2,on='product').merge(df3,on='product')
    df = ttal.drop_duplicates(subset=['product','price', 'CBD percentage'], keep='last')
         
        
    return df

def add_review(web, rev):
    filt = {"shop":{"$regex":f"{web}"}}
    project = {"_id":1, "product":0, "CBD percentage":0, "price":0}
    result = db.cbd_shops.find(filt, project)
    results= list(result)
    id_review = {}
    q = {"review": rev}
    results.append(q)
        
    for x in results:
           id_review.update(x)
    id_review["shop_id"] = id_review.pop("_id")
    
    return write_coll("db.cbd_product_review", id_review)

def read_reviews(web):
    filt = {"shop":{"$regex":f"{web}"}}
    project = {"_id":0, "shop_id":0, "shop":0}
    result = db.db.cbd_product_review.find(filt, project)
    results= list(result)

    return results