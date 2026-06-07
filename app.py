import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Netflix Analytics & AI Recommendation Platform",
    page_icon="🎬",
    layout="wide"
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.success("Netflix Analytics Platform v2.0")

st.sidebar.markdown("""
### Modules

📊 Dashboard

📈 Visualizations

🎯 Recommendations

💡 Insights

📄 Reports
""")

# =====================================
# SESSION STATE
# =====================================

if "df" not in st.session_state:
    st.session_state["df"] = None

# =====================================
# HEADER
# =====================================

st.title("🎬 Netflix Analytics & AI Recommendation Platform")

st.markdown("""
## Welcome

This platform provides advanced Netflix analytics,
machine learning recommendations, business insights,
data cleaning, reporting and predictive analytics.

---

### Key Features

✅ Interactive Dashboard

✅ Advanced Visualizations

✅ Business Intelligence Analytics

✅ Smart Insights Engine

✅ AI Recommendation System (TF-IDF)

✅ Data Cleaning & Preprocessing

✅ PDF Report Generation

---

### Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-Learn
- ReportLab

---

### Dataset

Netflix Movies and TV Shows Dataset

Upload your dataset using the sidebar to begin.
""")

# =====================================
# DATASET UPLOAD
# =====================================

st.sidebar.header("📂 Dataset Upload")

uploaded_file = st.sidebar.file_uploader(
    "Upload netflix_titles.csv",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        st.session_state["df"] = df

        st.sidebar.success(
            f"Dataset Loaded Successfully ({len(df)} records)"
        )

        st.sidebar.info(
            f"Columns Detected: {len(df.columns)}"
        )

    except Exception as e:

        st.sidebar.error(
            f"Dataset Error: {e}"
        )

# =====================================
# DATASET VALIDATION
# =====================================

if st.session_state["df"] is not None:

    df = st.session_state["df"]

    required_columns = [
        "title",
        "type",
        "country",
        "listed_in",
        "rating",
        "release_year",
        "description"
    ]

    missing_columns = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:

        st.error(
            f"Missing Required Columns: {missing_columns}"
        )

        st.stop()

# =====================================
# DATASET STATUS
# =====================================

if st.session_state["df"] is not None:

    df = st.session_state["df"]

    st.success(
        "✅ Dataset Loaded Successfully"
    )

    col1, col2, col3, col4 = st.columns(4)

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

    col4.metric(
        "Duplicate Rows",
        int(df.duplicated().sum())
    )

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    # =====================================
    # DATASET HEALTH SCORE
    # =====================================

    st.divider()

    st.subheader("📋 Dataset Health Score")

    total_cells = df.shape[0] * df.shape[1]

    missing_cells = df.isnull().sum().sum()

    health_score = round(
        ((total_cells - missing_cells) / total_cells) * 100,
        2
    )

    st.metric(
        "Dataset Quality Score",
        f"{health_score}%"
    )

else:

    st.warning(
        "Please upload netflix_titles.csv using the sidebar."
    )

# =====================================
# AVAILABLE MODULES
# =====================================

st.divider()

st.subheader("📌 Available Modules")

st.markdown("""
### 📊 Dashboard
- KPI Cards
- Advanced Filters
- Search Functionality
- Dataset Overview

### 📈 Visualizations
- Movies vs TV Shows
- Content Growth Trends
- Top Countries
- Genre Analytics
- Ratings Analytics

### 💡 Business Insights
- Executive Summary
- Strategic Recommendations
- Data Quality Analysis

### 🎯 AI Recommendation Engine
- TF-IDF Vectorization
- Cosine Similarity
- Content-Based Recommendations

### 🧹 Data Cleaning
- Missing Values Analysis
- Duplicate Detection

### 🧠 Smart Insights
- Automated Insights
- Business Intelligence

### 📄 Reports
- PDF Report Generation
- Executive Summaries
""")

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Built using Streamlit, Pandas, Plotly, Scikit-Learn and ReportLab."
)