import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🎬 Netflix Analytics Dashboard")

# =====================================
# LOAD DATA
# =====================================

df = st.session_state.get("df")

if df is None:
    st.warning(
        "Please upload netflix_titles.csv first."
    )
    st.stop()

# =====================================
# FILTERS
# =====================================

st.sidebar.header("🎛 Dashboard Filters")

content_type = st.sidebar.multiselect(
    "Content Type",
    sorted(
        df["type"]
        .dropna()
        .unique()
    )
)

ratings = st.sidebar.multiselect(
    "Rating",
    sorted(
        df["rating"]
        .dropna()
        .unique()
    )
)

filtered_df = df.copy()

if content_type:
    filtered_df = filtered_df[
        filtered_df["type"]
        .isin(content_type)
    ]

if ratings:
    filtered_df = filtered_df[
        filtered_df["rating"]
        .isin(ratings)
    ]

# =====================================
# SEARCH
# =====================================

st.subheader("🔍 Search Titles")

search = st.text_input(
    "Enter Title"
)

if search:

    results = filtered_df[
        filtered_df["title"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.success(
        f"{len(results)} titles found"
    )

    st.dataframe(
        results,
        width="stretch"
    )

# =====================================
# KPI CARDS
# =====================================

st.subheader("📊 Dashboard Overview")

total_titles = len(filtered_df)

movies = len(
    filtered_df[
        filtered_df["type"] == "Movie"
    ]
)

tvshows = len(
    filtered_df[
        filtered_df["type"] == "TV Show"
    ]
)

countries = (
    filtered_df["country"]
    .dropna()
    .nunique()
)

col1, col2, col3, col4 = st.columns(4)

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
    tvshows
)

col4.metric(
    "Countries",
    countries
)

# =====================================
# DATASET PREVIEW
# =====================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    width="stretch"
)

# =====================================
# TOP COUNTRIES
# =====================================

st.subheader("🌍 Top Countries")

country_data = (
    filtered_df["country"]
    .dropna()
    .value_counts()
    .head(10)
)

st.bar_chart(country_data)

# =====================================
# TOP GENRES
# =====================================

st.subheader("🎭 Top Genres")

genre_data = (
    filtered_df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

st.bar_chart(genre_data)

# =====================================
# EXECUTIVE SUMMARY
# =====================================

st.subheader("📈 Executive Summary")

st.success(
    f"""
Total Titles: {total_titles}

Movies: {movies}

TV Shows: {tvshows}

Countries Represented: {countries}
"""
)