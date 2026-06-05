import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Advanced Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Advanced Analytics")

# =====================================
# LOAD DATA FROM SESSION STATE
# =====================================

df = st.session_state.get("df")

if df is None:
    st.warning(
        "Please upload the Netflix dataset from the App page."
    )
    st.stop()

# =====================================
# KPI METRICS
# =====================================

total_titles = len(df)

movies = len(
    df[df["type"] == "Movie"]
)

tv_shows = len(
    df[df["type"] == "TV Show"]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Titles",
    total_titles
)

col2.metric(
    "Movies",
    movies
)

col3.metric(
    "TV Shows",
    tv_shows
)

# =====================================
# TOP DIRECTORS
# =====================================

st.subheader("🎬 Top 10 Directors")

directors = (
    df["director"]
    .dropna()
    .value_counts()
    .head(10)
)

fig1 = px.bar(
    x=directors.index,
    y=directors.values,
    title="Top Directors"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================
# TOP ACTORS
# =====================================

st.subheader("⭐ Top 10 Actors")

actors = (
    df["cast"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

fig2 = px.bar(
    x=actors.index,
    y=actors.values,
    title="Top Actors"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# TOP COUNTRIES
# =====================================

st.subheader("🌍 Top Countries")

countries = (
    df["country"]
    .dropna()
    .value_counts()
    .head(10)
)

fig3 = px.bar(
    x=countries.index,
    y=countries.values,
    title="Top Countries"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =====================================
# TOP GENRES
# =====================================

st.subheader("🎭 Top Genres")

genres = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

fig4 = px.bar(
    x=genres.index,
    y=genres.values,
    title="Top Genres"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =====================================
# ANALYTICS SUMMARY
# =====================================

st.subheader("📈 Analytics Summary")

top_director = directors.idxmax()
top_actor = actors.idxmax()
top_country = countries.idxmax()
top_genre = genres.idxmax()

st.success(
    f"""
Top Director: {top_director}

Top Actor: {top_actor}

Top Country: {top_country}

Top Genre: {top_genre}
"""
)