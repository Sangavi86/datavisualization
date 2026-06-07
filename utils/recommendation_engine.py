import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_recommendation_model(df):
    """
    Build TF-IDF similarity matrix using
    Netflix descriptions.
    """

    df = df.copy()

    if "description" not in df.columns:
        raise ValueError(
            "Dataset must contain a 'description' column."
        )

    df["description"] = (
        df["description"]
        .fillna("")
        .astype(str)
    )

    tfidf = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = tfidf.fit_transform(
        df["description"]
    )

    similarity_matrix = cosine_similarity(
        tfidf_matrix,
        tfidf_matrix
    )

    return similarity_matrix


def get_recommendations(
    title,
    df,
    similarity_matrix,
    top_n=5
):
    """
    Return top N recommended titles
    similar to selected title.
    """

    df = df.copy()

    df["title"] = (
        df["title"]
        .fillna("")
        .astype(str)
    )

    indices = pd.Series(
        df.index,
        index=df["title"]
    ).drop_duplicates()

    if title not in indices:
        return pd.DataFrame()

    idx = indices[title]

    similarity_scores = list(
        enumerate(
            similarity_matrix[idx]
        )
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[
        1: top_n + 1
    ]

    movie_indices = [
        i[0]
        for i in similarity_scores
    ]

    recommended_df = (
        df.iloc[movie_indices]
        .copy()
    )

    return recommended_df


def get_similar_titles(
    title,
    df,
    top_n=10
):
    """
    One-step recommendation function.
    """

    similarity_matrix = (
        build_recommendation_model(df)
    )

    return get_recommendations(
        title,
        df,
        similarity_matrix,
        top_n
    )