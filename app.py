import streamlit as st
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Netflix Analytics & Recommendation Platform",
    page_icon="🎬",
    layout="wide"
)

# =====================================
# SESSION STATE
# =====================================

if "df" not in st.session_state:
    st.session_state.df = None

# =====================================
# HEADER
# =====================================

st.title("🎬 Netflix Analytics & Recommendation Platform")

st.markdown("""
## Welcome

This project provides:

✅ Dashboard Analytics

✅ Interactive Visualizations

✅ Advanced Analytics

✅ Business Insights

✅ Recommendation System

✅ Data Cleaning

✅ Smart Insights

✅ Report Generation

---

### Features

- Netflix Content Analysis
- Genre Analytics
- Country Analytics
- Ratings Analysis
- Director Analytics
- Search Functionality
- Recommendation Engine
- Business Intelligence Insights
- Dataset Cleaning
- PDF Report Generation

---

### Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- NumPy

---
""")

# =====================================
# DATASET UPLOAD
# =====================================

st.sidebar.header("📂 Dataset Upload")

uploaded_file = st.sidebar.file_uploader(
    "Upload Netflix Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        st.session_state.df = df

        st.sidebar.success(
            f"Dataset Loaded ({len(df)} records)"
        )

    except Exception as e:

        st.sidebar.error(
            f"Error loading dataset: {e}"
        )

# =====================================
# DATASET STATUS
# =====================================

if st.session_state.df is not None:

    df = st.session_state.df

    st.success(
        "✅ Dataset Loaded Successfully"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Records",
        len(df)
    )

    col2.metric(
        "Columns",
        len(df.columns)
    )

    col3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

else:

    st.warning(
        "Please upload netflix_titles.csv using the sidebar."
    )

# =====================================
# PROJECT MODULES
# =====================================

st.divider()

st.subheader("📌 Available Modules")

st.markdown("""
### 📊 Dashboard
- KPI Cards
- Search Functionality
- Dataset Overview

### 📈 Visualizations
- Movies vs TV Shows
- Top Countries
- Genre Distribution
- Ratings Analysis
- Growth Trends

### 📊 Analytics
- Director Analytics
- Actor Analytics
- Country Analytics

### 💡 Insights
- Business Intelligence
- Statistical Insights

### 🎯 Recommendations
- Genre-Based Recommendations
- Title Search

### 🧹 Data Cleaning
- Missing Values Analysis
- Duplicate Detection

### 🧠 Smart Insights
- Automated Executive Insights
- Strategic Recommendations

### 📄 Reports
- PDF Report Generation
""")

st.info(
    "Use the pages in the left sidebar after uploading the dataset."
)