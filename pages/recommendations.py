import streamlit as st
import pandas as pd
import plotly.express as px

from utils.recommendation_engine import (
    build_recommendation_model,
    get_recommendations
)

st.set_page_config(
    page_title="AI Recommendation Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI-Powered Netflix Recommendation Engine")

# =====================================
# LOAD DATA
# =====================================

df = st.session_state.get("df")

if df is None:
    st.warning(
        "Please upload the Netflix dataset from the App page."
    )
    st.stop()

# =====================================
# BUILD AI MODEL
# =====================================

similarity_matrix = build_recommendation_model(df)

# =====================================
# TITLE SELECTION
# =====================================

st.subheader("🎬 Select a Netflix Title")

selected_title = st.selectbox(
    "Choose Movie / TV Show",
    sorted(
        df["title"]
        .dropna()
        .unique()
    )
)

# =====================================
# RECOMMENDATIONS
# =====================================

recommended_titles = get_recommendations(
    selected_title,
    df,
    similarity_matrix,
    top_n=5
)

st.subheader("🤖 Recommended Titles")

if not recommended_titles.empty:

    st.dataframe(
        recommended_titles[
            [
                "title",
                "type",
                "release_year",
                "rating",
                "country"
            ]
        ],
        use_container_width=True
    )

else:

    st.warning(
        "No recommendations available."
    )

# =====================================
# CONTENT SEARCH
# =====================================

st.subheader("🔍 Search Netflix Titles")

search = st.text_input(
    "Search Title"
)

if search:

    search_results = df[
        df["title"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        search_results,
        use_container_width=True
    )

# =====================================
# GENRE ANALYTICS
# =====================================

st.subheader("📈 Top Genres")

genre_data = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

fig1 = px.bar(
    x=genre_data.index,
    y=genre_data.values,
    title="Top 10 Genres"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================
# RATING ANALYTICS
# =====================================

st.subheader("⭐ Rating Distribution")

rating_data = (
    df["rating"]
    .dropna()
    .value_counts()
)

fig2 = px.pie(
    values=rating_data.values,
    names=rating_data.index,
    hole=0.4,
    title="Rating Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# AI EXPLANATION
# =====================================

st.subheader("🧠 How Recommendations Work")

st.info(
    """
This recommendation engine uses:

• TF-IDF Vectorization

• Cosine Similarity

• Content-Based Filtering

The system compares Netflix descriptions
and recommends titles that are most
similar to the selected title.
"""
)

# =====================================
# INSIGHTS
# =====================================

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

st.success(
    f"Most Popular Genre: {top_genre}"
)

st.success(
    f"Most Common Rating: {top_rating}"
)