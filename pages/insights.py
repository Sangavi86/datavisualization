import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Insights & Recommendations")

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

total_countries = (
    df["country"]
    .dropna()
    .nunique()
)

st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

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

col4.metric(
    "Countries",
    total_countries
)

# =====================================
# BUSINESS INSIGHTS
# =====================================

top_country = (
    df["country"]
    .dropna()
    .value_counts()
    .idxmax()
)

top_year = (
    df["release_year"]
    .value_counts()
    .idxmax()
)

top_rating = (
    df["rating"]
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

st.subheader("🔍 Key Insights")

st.success(
    f"🌍 Top Content Country: {top_country}"
)

st.success(
    f"📅 Peak Release Year: {top_year}"
)

st.success(
    f"⭐ Most Common Rating: {top_rating}"
)

st.success(
    f"🎭 Most Popular Genre: {top_genre}"
)

# =====================================
# EXECUTIVE SUMMARY
# =====================================

st.subheader("📈 Executive Summary")

st.info(
    f"""
Netflix hosts {total_titles} titles.

The majority of content comes from {top_country}.

The highest release activity occurred in {top_year}.

The most popular genre is {top_genre}.

The dominant audience rating is {top_rating}.
"""
)

# =====================================
# BUSINESS RECOMMENDATIONS
# =====================================

st.subheader("🚀 Business Recommendations")

st.markdown("""
### 1. Expand Regional Content
Increase content creation from underrepresented countries.

### 2. Invest in High-Performing Genres
Focus production on genres with strong popularity.

### 3. Improve Recommendation Systems
Use genre and rating preferences to personalize recommendations.

### 4. Balance Content Portfolio
Maintain a healthy mix of Movies and TV Shows.

### 5. Monitor Content Growth
Track release trends to optimize future investments.
""")

# =====================================
# DATA QUALITY REPORT
# =====================================

st.subheader("⚠ Data Quality Report")

missing_data = pd.DataFrame(
    df.isnull().sum(),
    columns=["Missing Values"]
)

st.dataframe(
    missing_data,
    use_container_width=True
)

# =====================================
# NUMERIC STATISTICS
# =====================================

st.subheader("📋 Numerical Statistics")

numeric_df = df.select_dtypes(
    include=["number"]
)

if not numeric_df.empty:

    st.dataframe(
        numeric_df.describe(),
        use_container_width=True
    )

else:

    st.warning(
        "No numeric columns available."
    )

# =====================================
# FINAL CONCLUSION
# =====================================

st.subheader("📌 Final Conclusion")

st.success(
    f"""
Netflix's content ecosystem is strongly influenced by {top_country}.

{top_genre} is the most dominant genre category.

The platform experienced peak releases in {top_year}.

Strategic investments should focus on audience preferences and regional content expansion.
"""
)