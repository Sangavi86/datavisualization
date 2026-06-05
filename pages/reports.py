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
# LOAD DATA FROM SESSION STATE
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

top_country = (
    df["country"]
    .dropna()
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

    content = []

    content.append(
        Paragraph(
            "Netflix Analytics Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Total Titles: {total_titles}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Movies: {total_movies}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"TV Shows: {total_tvshows}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Top Country: {top_country}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Top Genre: {top_genre}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Most Common Rating: {top_rating}",
            styles["BodyText"]
        )
    )

    doc.build(content)

    with open(
        temp_pdf.name,
        "rb"
    ) as pdf_file:

        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf_file,
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