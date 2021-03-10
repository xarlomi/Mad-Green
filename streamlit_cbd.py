import streamlit as st
from src.data_to_streamlit import *
import pandas as pd
import folium
import codecs
from streamlit_folium import folium_static
import streamlit.components.v1 as components
from PIL import Image
import altair as alt
import plotly.express as px
imagen = Image.open("images/imagen_header.jpg")
st.image(imagen, width=600)



st.write("""
# 🍁 Trip-Advisor-Madrid 🍁
**Tu comparador de precios de CBD en Madrid**
""")


st.write("### ¿Cómo te gustaría sentirte hoy 🚀?")
selected_mood = st.selectbox("Elije tu mood para encontrar tu mejor CBD-compañero", mood_list())

st.write(f"""#### ¡¡ Hay {count_cbd_mood(selected_mood)} tipos de CBD que te harán sentirte {selected_mood} !!
Fíltremos la búsqueda para encontrar tu match ideal: """)


st.write(f"### Aqui puedes encontrar dónde comprar {len(shop_mood(selected_mood))}  tipos de CBD que te hacen sentirte {selected_mood}:")
st.dataframe(merging_shop_rating(selected_mood))

st.write("""### ¿Todavía no sabes con cuál quedarte? 
**Déjate guiar por nuestros queridos usuarios... 🧙‍♂️:**""")
agree = st.button("Haz click aquí para ver las opiniones de estos buds")
if agree:
    df2 = shop_rating(selected_mood)
    fig = px.bar(df, x="product", y="rating", color="product", title=f"Los mejores tipos de CBD para sentirte {selected_mood} según nuestros usuarios:")
    fig.show()  

df = merging_shop_rating(selected_mood)    
makes = list(df['product'].drop_duplicates())
make_choice = st.sidebar.selectbox('Escoge el CBD  que mas te inspire:', makes)

cbd_per = list(df["CBD percentage"].loc[df["product"] == make_choice])
cbd_choice = st.sidebar.selectbox('Ahora elige % de CBD:', cbd_per)

prices = list(df["price"].loc[(df["product"] == make_choice) & (df["CBD percentage"]== cbd_choice)])
price_choice = st.sidebar.selectbox('Ahora por precio:', prices)



user_review = st.text_input("Añade tu comentario:")




