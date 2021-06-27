import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from add_data import db_execute_fetch
st.set_page_config(page_title="Dashboard", layout="wide")

import home
import bar
import hash
import lang
PAGES = {
    "Home Page" : home,
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