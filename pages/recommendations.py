import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Netflix Recommendations",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Netflix Recommendation System")

df = st.session_state.get("df")

if df is None:
    st.warning(
        "Please upload the Netflix dataset from the App page."
    )
    st.stop()

# ==================================
# Genre Based Recommendation
# ==================================

st.header("🎭 Genre-Based Recommendations")

genres = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .unique()
)

selected_genre = st.selectbox(
    "Select Genre",
    sorted(genres)
)

recommendations = df[
    df["listed_in"]
    .str.contains(
        selected_genre,
        case=False,
        na=False
    )
]

st.success(
    f"{len(recommendations)} titles found in {selected_genre}"
)

st.dataframe(
    recommendations[
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

# ==================================
# Search Recommendation
# ==================================

st.header("🔍 Search Netflix Titles")

search_title = st.text_input(
    "Enter Title Name"
)

if search_title:

    search_results = df[
        df["title"]
        .str.contains(
            search_title,
            case=False,
            na=False
        )
    ]

    st.write(
        f"Found {len(search_results)} matching titles"
    )

    st.dataframe(
        search_results[
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

# ==================================
# Top Genres
# ==================================

st.header("📈 Popular Genres")

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

# ==================================
# Rating Distribution
# ==================================

st.header("⭐ Rating Distribution")

rating_data = (
    df["rating"]
    .dropna()
    .value_counts()
)

fig2 = px.pie(
    values=rating_data.values,
    names=rating_data.index,
    hole=0.4,
    title="Ratings Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================
# Recommendation Insights
# ==================================

st.header("💡 Recommendation Insights")

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