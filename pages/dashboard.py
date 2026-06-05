import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🎬 Netflix Analytics Dashboard")

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
# SIDEBAR FILTERS
# =====================================

st.sidebar.header("Dashboard Filters")

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
        filtered_df["type"].isin(content_type)
    ]

if ratings:
    filtered_df = filtered_df[
        filtered_df["rating"].isin(ratings)
    ]

# =====================================
# SEARCH
# =====================================

st.subheader("🔍 Search Netflix Titles")

search = st.text_input(
    "Enter Movie or TV Show Name"
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
        use_container_width=True
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

tv_shows = len(
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
    tv_shows
)

col4.metric(
    "Countries",
    countries
)

# =====================================
# DATASET INFO
# =====================================

st.subheader("📁 Dataset Information")

info1, info2, info3 = st.columns(3)

info1.info(
    f"Rows: {filtered_df.shape[0]}"
)

info2.info(
    f"Columns: {filtered_df.shape[1]}"
)

info3.info(
    f"Missing Values: {int(filtered_df.isnull().sum().sum())}"
)

# =====================================
# DATASET PREVIEW
# =====================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

# =====================================
# MISSING VALUES
# =====================================

st.subheader("⚠ Missing Values")

missing_df = pd.DataFrame(
    filtered_df.isnull().sum(),
    columns=["Missing Count"]
)

st.dataframe(
    missing_df,
    use_container_width=True
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

st.dataframe(
    country_data,
    use_container_width=True
)

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

st.dataframe(
    genre_data,
    use_container_width=True
)

# =====================================
# EXECUTIVE SUMMARY
# =====================================

st.subheader("📈 Executive Summary")

st.success(
    f"""
Dataset contains {total_titles} Netflix titles.

Movies: {movies}

TV Shows: {tv_shows}

Countries Represented: {countries}
"""
)