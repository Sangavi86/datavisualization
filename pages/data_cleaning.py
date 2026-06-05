import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Cleaning",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Data Cleaning & Preprocessing")

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
# DATASET OVERVIEW
# =====================================

st.subheader("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Rows",
    df.shape[0]
)

col2.metric(
    "Columns",
    df.shape[1]
)

col3.metric(
    "Missing Values",
    int(df.isnull().sum().sum())
)

st.dataframe(
    df.head(),
    use_container_width=True
)

st.divider()

# =====================================
# MISSING VALUES ANALYSIS
# =====================================

st.subheader("⚠ Missing Values Analysis")

missing_values = pd.DataFrame(
    df.isnull().sum(),
    columns=["Missing Values"]
)

st.dataframe(
    missing_values,
    use_container_width=True
)

st.divider()

# =====================================
# DUPLICATE ANALYSIS
# =====================================

st.subheader("🔁 Duplicate Records")

duplicates = df.duplicated().sum()

st.warning(
    f"Duplicate Rows Found: {duplicates}"
)

st.divider()

# =====================================
# CLEANING OPERATIONS
# =====================================

st.subheader("🧹 Cleaning Operations")

col1, col2 = st.columns(2)

with col1:

    if st.button("Remove Duplicates"):

        cleaned_df = df.drop_duplicates()

        st.success(
            "Duplicates Removed Successfully!"
        )

        st.write(
            f"New Shape: {cleaned_df.shape}"
        )

        st.dataframe(
            cleaned_df.head(),
            use_container_width=True
        )

with col2:

    if st.button("Fill Missing Values"):

        cleaned_df = df.fillna(
            "Unknown"
        )

        st.success(
            "Missing Values Filled Successfully!"
        )

        st.dataframe(
            cleaned_df.head(),
            use_container_width=True
        )

st.divider()

# =====================================
# CLEAN DATASET PREVIEW
# =====================================

st.subheader("✅ Clean Dataset Preview")

cleaned_df = (
    df
    .drop_duplicates()
    .fillna("Unknown")
)

st.dataframe(
    cleaned_df.head(20),
    use_container_width=True
)

# =====================================
# CLEANING SUMMARY
# =====================================

st.subheader("📋 Cleaning Summary")

original_rows = len(df)

clean_rows = len(cleaned_df)

removed_rows = (
    original_rows - clean_rows
)

st.success(
    f"""
Original Rows: {original_rows}

Cleaned Rows: {clean_rows}

Rows Removed: {removed_rows}

Missing Values Filled: Yes
"""
)

# =====================================
# DOWNLOAD CLEAN DATASET
# =====================================

st.subheader("⬇ Download Clean Dataset")

csv = cleaned_df.to_csv(
    index=False
)

st.download_button(
    label="Download Clean Dataset",
    data=csv,
    file_name="clean_netflix_dataset.csv",
    mime="text/csv"
)