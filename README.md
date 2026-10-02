# Final Data Analytics Project — SWYNEX Internship

## 1. Problem Statement
Organizations need clean, well-analyzed employee data to make informed HR and business decisions. This project takes a raw, messy employee dataset through a complete analytics pipeline — from cleaning to visualization — to uncover actionable insights about workforce salary trends, performance, and distribution.

## 2. Dataset Information
- **Source**: Messy Employee Dataset (Kaggle) — https://www.kaggle.com/datasets/desolution01/messy-employee-dataset
- **Records**: ~1020 employees
- **Columns**: Employee_ID, First_Name, Last_Name, Age, Department_Region, Status, Join_Date, Salary, Email, Phone, Performance_Score, Remote_Work
- **Issues in raw data**: Missing values, duplicate records, inconsistent text casing, mixed date formats

## 3. Data Cleaning Process (Task 1)
Performed using Python (pandas):
- Removed duplicate records
- Filled missing values (median for numeric, 'Unknown' for text fields)
- Converted Join_Date to proper datetime format
- Standardized text casing and whitespace
- Standardized Remote_Work values to consistent Yes/No format
- Removed records with missing critical fields (Employee_ID)

📁 Folder: `data-cleaning/`

## 4. Exploratory Data Analysis (Task 2)
Performed using Python (pandas, matplotlib, seaborn):
- Summary statistics and data distribution analysis
- Salary analysis by Department/Region
- Age distribution analysis
- Performance score patterns by remote work status
- Status breakdown and outlier detection (IQR method)

📁 Folder: `eda/`

## 5. Interactive Dashboard (Task 3)
Built using Streamlit and Plotly:
- Real-time KPIs (Total Employees, Average Salary, Average Age, Remote Count)
- Interactive filters (Department/Region, Status, Remote Work)
- 6 dynamic visualizations
- Filterable data table

📁 Folder: `dashboard/`

## 6. Key Business Insights
1. **Salary Disparity**: Significant salary variation exists across departments/regions, with [highest] earning notably more than [lowest] — worth reviewing for pay equity.
2. **Workforce Age**: The average employee age is ~32 years, indicating a relatively young, early-to-mid career workforce.
3. **Remote Work & Performance**: Performance score distribution differs between remote and non-remote employees, suggesting remote work policy may be influencing output or measurement.
4. **Employee Concentration**: A few departments/regions account for a disproportionate share of the workforce, which could indicate hiring imbalance or regional business focus.
5. **Retention Signal**: The status breakdown shows [X]% active vs [inactive/other], offering an early view into attrition patterns.
6. **Data Quality**: Several salary outliers were detected, which may represent either genuine high earners or data entry errors requiring HR review.

## 7. Recommendations
- Review salary bands across departments for fairness and retention risk
- Investigate root cause of performance differences between remote/non-remote employees
- Use the dashboard for ongoing monitoring rather than one-time analysis

## 8. Tools & Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, Streamlit, Plotly, Git/GitHub

## 9. Project Structure
SWYNEX-Final-Data-Analytics-Project/
├── data-cleaning/      # Task 1: Raw data cleaning
├── eda/                # Task 2: Exploratory analysis
├── dashboard/          # Task 3: Interactive Streamlit dashboard
└── README.md           # This file — full case study
## 10. Author
Anand Kotapati
GitHub: https://github.com/anandkotapati-rgb
LinkedIn: https://linkedin.com/in/anand-kotapati-b28aa92a9