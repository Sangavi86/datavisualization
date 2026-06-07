import streamlit as st
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="Prediction Center",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Netflix Prediction Center")

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
# DATA VALIDATION
# =====================================

required_columns = [
    "type",
    "rating",
    "country"
]

for col in required_columns:

    if col not in df.columns:

        st.error(
            f"Required column '{col}' not found."
        )

        st.stop()

# =====================================
# PREPARE DATA
# =====================================

data = df[
    [
        "type",
        "rating",
        "country"
    ]
].dropna()

encoder_rating = LabelEncoder()
encoder_country = LabelEncoder()
encoder_type = LabelEncoder()

data["rating"] = (
    encoder_rating.fit_transform(
        data["rating"]
    )
)

data["country"] = (
    encoder_country.fit_transform(
        data["country"]
    )
)

data["type"] = (
    encoder_type.fit_transform(
        data["type"]
    )
)

X = data[
    [
        "rating",
        "country"
    ]
]

y = data["type"]

# =====================================
# TRAIN MODEL
# =====================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X,
    y
)

# =====================================
# USER INPUTS
# =====================================

st.subheader(
    "🎯 Predict Content Type"
)

selected_rating = st.selectbox(
    "Select Rating",
    sorted(
        df["rating"]
        .dropna()
        .unique()
    )
)

selected_country = st.selectbox(
    "Select Country",
    sorted(
        df["country"]
        .dropna()
        .unique()
    )
)

# =====================================
# PREDICTION
# =====================================

if st.button(
    "Predict"
):

    rating_encoded = (
        encoder_rating.transform(
            [selected_rating]
        )[0]
    )

    country_encoded = (
        encoder_country.transform(
            [selected_country]
        )[0]
    )

    prediction = model.predict(
        [[
            rating_encoded,
            country_encoded
        ]]
    )

    result = (
        encoder_type.inverse_transform(
            prediction
        )[0]
    )

    st.success(
        f"Predicted Content Type: {result}"
    )

# =====================================
# MODEL INFO
# =====================================

st.subheader(
    "🧠 Machine Learning Information"
)

st.info(
    """
Algorithm Used:
• Random Forest Classifier

Input Features:
• Rating
• Country

Prediction:
• Movie
• TV Show
"""
)

# =====================================
# DATA OVERVIEW
# =====================================

st.subheader(
    "📊 Training Dataset"
)

st.dataframe(
    data.head(20),
    width="stretch"
)