import streamlit as st
import numpy as np
import streamlit as st
import altair as alt
import pandas as pd
from add_data import db_execute_fetch


def app():
    st.title('APP2')
    st.write('Welcome to app2')


def app():
    st.title('#HashTags')
    st.write('You can see Ranking here')
    selectHashTag()
    st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)


def loadData():
    query = "select * from TweetInformation"
    df = db_execute_fetch(query, dbName="tweets", rdf=True)
    return df


def selectHashTag():
    df = loadData()
    hashTags = st.multiselect("choose combaniation of hashtags", list(df['hashtags'].unique()))
    if hashTags:
        df = df[np.isin(df, hashTags).any(axis=1)]
        st.write(df)

