import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Netflix Visualizations Dashboard")

# =====================================
# LOAD DATA FROM SESSION STATE
# =====================================

df = st.session_state.get("df")

if df is None:
    st.warning(
        "Please upload the Netflix dataset from the main App page."
    )
    st.stop()

# =====================================
# SIDEBAR FILTERS
# =====================================

st.sidebar.header("Visualization Filters")

content_type = st.sidebar.multiselect(
    "Content Type",
    sorted(
        df["type"]
        .dropna()
        .unique()
    )
)

rating_filter = st.sidebar.multiselect(
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

if rating_filter:
    filtered_df = filtered_df[
        filtered_df["rating"].isin(rating_filter)
    ]

# =====================================
# MOVIES VS TV SHOWS
# =====================================

st.subheader("🎬 Movies vs TV Shows")

content = (
    filtered_df["type"]
    .value_counts()
)

fig1 = px.pie(
    values=content.values,
    names=content.index,
    hole=0.4,
    title="Content Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================
# CONTENT GROWTH TREND
# =====================================

st.subheader("📈 Netflix Content Growth")

year_data = (
    filtered_df["release_year"]
    .value_counts()
    .sort_index()
)

fig2 = px.line(
    x=year_data.index,
    y=year_data.values,
    markers=True,
    labels={
        "x": "Release Year",
        "y": "Number of Titles"
    },
    title="Content Released Per Year"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# TOP COUNTRIES
# =====================================

st.subheader("🌍 Top 10 Countries")

country_data = (
    filtered_df["country"]
    .dropna()
    .value_counts()
    .head(10)
)

fig3 = px.bar(
    x=country_data.index,
    y=country_data.values,
    title="Top Countries by Content"
)

st.plotly_chart(
    fig3,
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

fig4 = px.bar(
    x=genre_data.index,
    y=genre_data.values,
    title="Top 10 Genres"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =====================================
# RATINGS DISTRIBUTION
# =====================================

st.subheader("⭐ Ratings Distribution")

rating_data = (
    filtered_df["rating"]
    .dropna()
    .value_counts()
)

fig5 = px.bar(
    x=rating_data.index,
    y=rating_data.values,
    title="Ratings Distribution"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# =====================================
# CONTENT BY YEAR TABLE
# =====================================

st.subheader("📅 Content Release Analysis")

year_table = pd.DataFrame({
    "Year": year_data.index,
    "Titles Released": year_data.values
})

st.dataframe(
    year_table,
    use_container_width=True
)

# =====================================
# VISUALIZATION SUMMARY
# =====================================

st.subheader("📊 Visualization Summary")

top_country = (
    filtered_df["country"]
    .dropna()
    .value_counts()
    .idxmax()
)

top_genre = (
    filtered_df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .idxmax()
)

st.success(
    f"""
Top Content Country: {top_country}

Most Popular Genre: {top_genre}

Total Titles Visualized: {len(filtered_df)}
"""
)