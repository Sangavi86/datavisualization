import streamlit as st
import pandas as pd


def load_dataset():

    if "df" not in st.session_state:
        st.session_state.df = None

    return st.session_state.df


def save_dataset(df):

    st.session_state.df = df


def is_dataset_loaded():

    return (
        "df" in st.session_state
        and st.session_state.df is not None
    )