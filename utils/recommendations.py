import pandas as pd


def get_genre_recommendations(
    df,
    genre
):

    recommendations = df[
        df["listed_in"]
        .str.contains(
            genre,
            case=False,
            na=False
        )
    ]

    return recommendations[
        [
            "title",
            "type",
            "release_year",
            "rating",
            "country"
        ]
    ]


def search_titles(
    df,
    title
):

    results = df[
        df["title"]
        .str.contains(
            title,
            case=False,
            na=False
        )
    ]

    return results


def top_genres(df):

    return (
        df["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )