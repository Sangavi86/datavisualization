import streamlit as st
import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Netflix Analytics Report Generator")

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
# DATASET SUMMARY
# =====================================

st.subheader("📊 Dataset Summary")

total_titles = len(df)

total_movies = len(
    df[df["type"] == "Movie"]
)

total_tvshows = len(
    df[df["type"] == "TV Show"]
)

country_counts = (
    df["country"]
    .dropna()
    .value_counts()
)

top_country = (
    country_counts.idxmax()
    if not country_counts.empty
    else "N/A"
)

rating_counts = (
    df["rating"]
    .dropna()
    .value_counts()
)

top_rating = (
    rating_counts.idxmax()
    if not rating_counts.empty
    else "N/A"
)

genre_counts = (
    df["listed_in"]
    .dropna()
    .astype(str)
    .str.split(", ")
    .explode()
    .value_counts()
)

top_genre = (
    genre_counts.idxmax()
    if not genre_counts.empty
    else "N/A"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Titles",
        total_titles
    )

with col2:
    st.metric(
        "Movies",
        total_movies
    )

with col3:
    st.metric(
        "TV Shows",
        total_tvshows
    )

st.metric(
    "Top Country",
    top_country
)

# =====================================
# REPORT PREVIEW
# =====================================

st.subheader("📋 Report Preview")

st.info(
    f"""
Total Titles: {total_titles}

Movies: {total_movies}

TV Shows: {total_tvshows}

Top Country: {top_country}

Top Genre: {top_genre}

Most Common Rating: {top_rating}
"""
)

# =====================================
# PDF GENERATION
# =====================================

if st.button("Generate PDF Report"):

    temp_pdf = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    doc = SimpleDocTemplate(
        temp_pdf.name
    )

    styles = getSampleStyleSheet()

    content = [
        Paragraph(
            "Netflix Analytics Report",
            styles["Title"]
        ),
        Spacer(1, 12),
        Paragraph(
            f"Total Titles: {total_titles}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Movies: {total_movies}",
            styles["BodyText"]
        ),
        Paragraph(
            f"TV Shows: {total_tvshows}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Top Country: {top_country}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Top Genre: {top_genre}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Most Common Rating: {top_rating}",
            styles["BodyText"]
        )
    ]

    doc.build(content)

    with open(
        temp_pdf.name,
        "rb"
    ) as pdf_file:

        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf_file.read(),
            file_name="Netflix_Analytics_Report.pdf",
            mime="application/pdf"
        )

# =====================================
# EXECUTIVE SUMMARY
# =====================================

st.subheader("📈 Executive Summary")

st.success(
    f"""
Netflix currently hosts {total_titles} titles.

The platform is dominated by content from {top_country}.

The most popular genre is {top_genre}.

The most common audience rating is {top_rating}.

Movies account for the majority of the catalog.
"""
)