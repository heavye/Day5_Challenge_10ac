import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from add_data import db_execute_fetch
st.set_page_config(page_title="Dashboard", layout="wide")

import bar
import hash
import lang
PAGES = {
    "Bar Chart ": bar,
    "Hash Tags": hash,
    "Languages" : lang
}
st.sidebar.title('Pages')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()


#Loading data from the database
def loadData():
    query = "select * from TweetInformation"
    df = db_execute_fetch(query, dbName="tweets", rdf=True)
    return df


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



def wordCloud():
    df = loadData()
    cleanText = ''
    for text in df['clean_text']:
        tokens = str(text).lower().split()

        cleanText += " ".join(tokens) + " "

    wc = WordCloud(width=650, height=450, background_color='white', min_font_size=5).generate(cleanText)
    st.title("Tweet Text Word Cloud")
    st.image(wc.to_array())





selectLocAndAuth()
st.title("Data Visualizations")
wordCloud()

