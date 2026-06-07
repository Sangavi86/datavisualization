import streamlit as st
import pandas as pd
import plotly.express as px

from textblob import TextBlob

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="wide"
)

st.title("😊 Netflix Sentiment Analysis")

# =====================================
# UPLOAD REVIEW DATASET
# =====================================

uploaded_file = st.file_uploader(
    "Upload Review Dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success(
        f"Dataset Loaded Successfully ({len(df)} records)"
    )

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(),
        width="stretch"
    )

    # =====================================
    # SELECT TEXT COLUMN
    # =====================================

    text_column = st.selectbox(
        "Select Review Column",
        df.columns
    )

    # =====================================
    # SENTIMENT FUNCTION
    # =====================================

    def analyze_sentiment(text):

        polarity = TextBlob(
            str(text)
        ).sentiment.polarity

        if polarity > 0:
            return "Positive"

        elif polarity < 0:
            return "Negative"

        else:
            return "Neutral"

    df["Sentiment"] = (
        df[text_column]
        .apply(analyze_sentiment)
    )

    # =====================================
    # RESULTS
    # =====================================

    st.subheader(
        "Sentiment Results"
    )

    st.dataframe(
        df.head(20),
        width="stretch"
    )

    # =====================================
    # SENTIMENT DISTRIBUTION
    # =====================================

    sentiment_counts = (
        df["Sentiment"]
        .value_counts()
    )

    fig = px.pie(
        values=sentiment_counts.values,
        names=sentiment_counts.index,
        title="Sentiment Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # =====================================
    # KPIs
    # =====================================

    positive = (
        sentiment_counts.get(
            "Positive",
            0
        )
    )

    negative = (
        sentiment_counts.get(
            "Negative",
            0
        )
    )

    neutral = (
        sentiment_counts.get(
            "Neutral",
            0
        )
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Positive Reviews",
        positive
    )

    col2.metric(
        "Negative Reviews",
        negative
    )

    col3.metric(
        "Neutral Reviews",
        neutral
    )

else:

    st.info(
        "Upload a review dataset to perform sentiment analysis."
    )