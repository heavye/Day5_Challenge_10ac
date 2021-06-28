import streamlit as st
import numpy as np
import plotly.express as px
import streamlit as st
import altair as alt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image
from wordcloud import WordCloud
from add_data import db_execute_fetch


def app():
    st.title('APP2')
    st.write('Welcome to app2')


def app():
    st.title('Twitter Data Visualisation ')
    st.write(' By : Euel Fantaye ')
    wordCloud()
    selectLocAndAuth()


def loadData():
    query = "select * from TweetInformation"
    df = db_execute_fetch(query, dbName="tweets", rdf=True)
    return df


def wordCloud():
    df = loadData()
    cleanText = ''
    for text in df['clean_text']:
        tokens = str(text).lower().split()

        cleanText += " ".join(tokens) + " "
    mask = np.array(Image.open("mask.jpg"))
    colors = ["#FF0000", "#002868", "#BA55D3","#FAF0E6","#00FF00","#FF4500","#FFFF00"]
    cmap = LinearSegmentedColormap.from_list("mycmap", colors)
    wc = WordCloud(width=650, height=450, background_color='black', colormap=cmap , mask=mask,  min_font_size=5).generate(cleanText)
    st.title("Tweet Text Word Cloud")
    st.image(wc.to_array())


def selectLocAndAuth():
    df = loadData()
    location = st.multiselect("choose Location of tweets", list(df['place_coordinate'].unique()))
    lang = st.multiselect("choose Language of tweets", list(df['language'].unique()))

    if location and not lang:
        df = df[np.isin(df, location).any(axis=1)]
        st.write(df)
    elif lang and not location:
        df = df[np.isin(df, lang).any(axis=1)]
        st.write(df)
    elif lang and location:
        location.extend(lang)
        df = df[np.isin(df, location).any(axis=1)]
        st.write(df)
    else:
        st.write(df)