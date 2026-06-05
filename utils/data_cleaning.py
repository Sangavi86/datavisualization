import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """

    return df.drop_duplicates()


def fill_missing_values(df):
    """
    Fill missing values with 'Unknown'.
    """

    return df.fillna("Unknown")


def get_missing_values(df):
    """
    Return missing value report.
    """

    return pd.DataFrame(
        df.isnull().sum(),
        columns=["Missing Values"]
    )


def clean_dataset(df):
    """
    Complete cleaning pipeline.
    """

    cleaned_df = (
        df
        .drop_duplicates()
        .fillna("Unknown")
    )

    return cleaned_df


def get_dataset_summary(df):
    """
    Return dataset statistics.
    """

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }

    return summary