import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Employee Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/cleaned_data.csv')
    return df

df = load_data()

# Title
st.title("📊 Employee Analytics Dashboard")
st.markdown("Interactive dashboard built for SWYNEX Internship — Task 3")

# ===== SIDEBAR FILTERS =====
st.sidebar.header("Filters")

dept_filter = st.sidebar.multiselect(
    "Select Department/Region",
    options=df['Department_Region'].unique(),
    default=df['Department_Region'].unique()
)

status_filter = st.sidebar.multiselect(
    "Select Status",
    options=df['Status'].unique(),
    default=df['Status'].unique()
)

remote_filter = st.sidebar.multiselect(
    "Remote Work",
    options=df['Remote_Work'].unique(),
    default=df['Remote_Work'].unique()
)

# Apply filters
filtered_df = df[
    (df['Department_Region'].isin(dept_filter)) &
    (df['Status'].isin(status_filter)) &
    (df['Remote_Work'].isin(remote_filter))
]

# ===== KPIs =====
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", len(filtered_df))
col2.metric("Average Salary", f"₹{filtered_df['Salary'].mean():,.0f}")
col3.metric("Average Age", f"{filtered_df['Age'].mean():.1f} yrs")
col4.metric("Remote Employees", f"{(filtered_df['Remote_Work'] == 'True').sum()}")

st.markdown("---")

# ===== CHARTS ROW 1 =====
col1, col2 = st.columns(2)

with col1:
    st.subheader("Average Salary by Department/Region")
    dept_salary = filtered_df.groupby('Department_Region')['Salary'].mean().sort_values(ascending=False).reset_index()
    fig1 = px.bar(dept_salary, x='Department_Region', y='Salary', color='Salary', color_continuous_scale='Blues')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Employee Count by Department/Region")
    dept_count = filtered_df['Department_Region'].value_counts().reset_index()
    dept_count.columns = ['Department_Region', 'Count']
    fig2 = px.pie(dept_count, names='Department_Region', values='Count', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

# ===== CHARTS ROW 2 =====
col1, col2 = st.columns(2)

with col1:
    st.subheader("Age Distribution")
    fig3 = px.histogram(filtered_df, x='Age', nbins=20, color_discrete_sequence=['coral'])
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("Status Breakdown")
    status_count = filtered_df['Status'].value_counts().reset_index()
    status_count.columns = ['Status', 'Count']
    fig4 = px.pie(status_count, names='Status', values='Count')
    st.plotly_chart(fig4, use_container_width=True)

# ===== CHARTS ROW 3 =====
col1, col2 = st.columns(2)

with col1:
    st.subheader("Performance Score Distribution by Remote Work")
    perf_data = filtered_df.groupby(['Remote_Work', 'Performance_Score']).size().reset_index(name='Count')
    fig5 = px.bar(perf_data, x='Remote_Work', y='Count', color='Performance_Score', barmode='group')
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    st.subheader("Salary vs Age")
    fig6 = px.scatter(filtered_df, x='Age', y='Salary', color='Department_Region', size='Performance_Score' if filtered_df['Performance_Score'].dtype != object else None)
    st.plotly_chart(fig6, use_container_width=True)

# ===== DATA TABLE =====
st.markdown("---")
st.subheader("Filtered Employee Data")
st.dataframe(filtered_df, use_container_width=True)