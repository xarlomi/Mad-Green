import streamlit as st
from src.data_to_streamlit import *

import pandas as pd
import folium
import codecs
from streamlit_folium import folium_static
import streamlit.components.v1 as components


st.write("""
# Mad-Green
Comparador de precios de CBD Madrid
""")

mood = st.selectbox("## ¿Cómo te gustaría sentirte hoy 🚀?", mood_list())

st.write(f"## Hay {count_cbd_mood(mood)} con ese {mood}"
)
