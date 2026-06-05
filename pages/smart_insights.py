import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Insights",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Smart Insights & Business Intelligence")

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

total_movies = len(
    df[df["type"] == "Movie"]
)

total_tvshows = len(
    df[df["type"] == "TV Show"]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Titles",
    total_titles
)

col2.metric(
    "Movies",
    total_movies
)

col3.metric(
    "TV Shows",
    total_tvshows
)

# =====================================
# SMART INSIGHTS
# =====================================

top_country = (
    df["country"]
    .dropna()
    .value_counts()
    .idxmax()
)

top_genre = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .idxmax()
)

top_rating = (
    df["rating"]
    .dropna()
    .value_counts()
    .idxmax()
)

peak_year = (
    df["release_year"]
    .value_counts()
    .idxmax()
)

st.subheader("📊 AI-Generated Insights")

st.success(
    f"🌍 Most content originates from: {top_country}"
)

st.success(
    f"🎭 Most popular genre: {top_genre}"
)

st.success(
    f"⭐ Most common audience rating: {top_rating}"
)

st.success(
    f"📅 Peak release year: {peak_year}"
)

# =====================================
# CONTENT DISTRIBUTION
# =====================================

st.subheader("📈 Content Distribution")

movie_percentage = round(
    (total_movies / total_titles) * 100,
    2
)

tv_percentage = round(
    (total_tvshows / total_titles) * 100,
    2
)

col1, col2 = st.columns(2)

col1.metric(
    "Movies %",
    f"{movie_percentage}%"
)

col2.metric(
    "TV Shows %",
    f"{tv_percentage}%"
)

# =====================================
# EXECUTIVE SUMMARY
# =====================================

st.subheader("📋 Executive Summary")

st.info(
    f"""
Netflix currently hosts {total_titles} titles.

The majority of content is produced in {top_country}.

The platform's most popular genre is {top_genre}.

Audience engagement is highest within the {top_rating} rating category.

The highest content production occurred in {peak_year}.
"""
)

# =====================================
# BUSINESS RECOMMENDATIONS
# =====================================

st.subheader("🚀 Strategic Recommendations")

recommendations = [
    "Increase investment in high-performing genres.",
    "Expand content production in emerging markets.",
    "Improve recommendation systems using audience preferences.",
    "Create more regional language content.",
    "Maintain a balance between Movies and TV Shows."
]

for rec in recommendations:
    st.write("✅", rec)

# =====================================
# KEY FINDINGS TABLE
# =====================================

st.subheader("📊 Key Findings")

findings = pd.DataFrame(
    {
        "Metric": [
            "Top Country",
            "Top Genre",
            "Top Rating",
            "Peak Year",
            "Movies %",
            "TV Shows %"
        ],
        "Value": [
            top_country,
            top_genre,
            top_rating,
            peak_year,
            f"{movie_percentage}%",
            f"{tv_percentage}%"
        ]
    }
)

st.dataframe(
    findings,
    use_container_width=True
)

# =====================================
# FINAL CONCLUSION
# =====================================

st.subheader("📌 Final Conclusion")

st.success(
    f"""
Netflix's growth is strongly driven by content from {top_country}.

The dominant genre category is {top_genre}.

Future business expansion should focus on audience preferences,
regional content production, and personalized recommendations.
"""
)