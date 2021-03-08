import streamlit as st
from src.data_to_streamlit import *
import pandas as pd
import folium
import codecs
from streamlit_folium import folium_static
import streamlit.components.v1 as components
from PIL import Image
import altair as alt
imagen = Image.open("images/imagen_header.jpg")
st.image(imagen)



st.write("""
# Mad-Green
**Tu comparador de precios de CBD en Madrid**
""")


st.write("### ¿Cómo te gustaría sentirte hoy 🚀?")
selected_mood = st.selectbox("Elije tu mood para encontrar tu mejor CBD-compañero", mood_list())

st.write(f"#### Hay {count_cbd_mood(selected_mood)} tipos de CBD que te harán sentirte {selected_mood}")


st.write(f"### Aqui puedes comprar los tipos de CBD que te hacen sentirte {selected_mood}:")
st.dataframe(shop_mood(selected_mood))





