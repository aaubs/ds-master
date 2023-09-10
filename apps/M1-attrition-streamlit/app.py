# Import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load the dataset
@st.cache_data  # Cache the function to enhance performance
def load_data():
    # Define the file path
    file_path = 'https://raw.githubusercontent.com/aaubs/ds-master/main/apps/M1-attrition-streamlit/HR-Employee-Attrition.csv'
    
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv(file_path)

    # Create age groups and add as a new column
    bin_edges = [18, 25, 35, 45, 60]
    bin_labels = ['18-24', '25-34', '35-44', '45-60']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bin_edges, labels=bin_labels, right=False)

    return df

# Load the data using the defined function
df = load_data()

# Set the app title and sidebar header
st.title("Employee Attrition Dashboard 😊📈")
st.sidebar.header("Filters 📊")

# Introduction

# HR Attrition Dashboard

st.markdown("""
            Welcome to the HR Attrition Dashboard. In the backdrop of rising employee turnovers, HR departments are stressing the significance of predicting and understanding employee departures. Through the lens of data analytics, this dashboard unveils the deeper causes of employee churn and proposes strategies to boost employee retention.
""")
with st.expander("📊 **Objective**"):
                 st.markdown("""
At the heart of this dashboard is the mission to visually decode data, equipping HR experts with insights to tackle these queries:
- Which company factions face a greater likelihood of employee exits?
- What might be pushing these individuals to part ways?
- Observing the discerned trends, what incentives might hold the key to decreasing the attrition rate?
"""
)
                             
# Tutorial Expander
with st.expander("How to Use the Dashboard 📚"):
    st.markdown("""
    1. **Filter Data** - Use the sidebar filters to narrow down specific data sets.
    2. **Visualize Data** - From the dropdown, select a visualization type to view patterns.
    3. **Insights & Recommendations** - Scroll down to see insights derived from the visualizations and actionable recommendations.
    """)


# Sidebar filter: Age Group
selected_age_group = st.sidebar.multiselect("Select Age Groups 🕰️", df['AgeGroup'].unique().tolist(), default=df['AgeGroup'].unique().tolist())
if not selected_age_group:
    st.warning("Please select an age group from the sidebar ⚠️")
    st.stop()
filtered_df = df[df['AgeGroup'].isin(selected_age_group)]

# Sidebar filter: Department
departments = df['Department'].unique().tolist()
selected_department = st.sidebar.multiselect("Select Departments 🏢", departments, default=departments)
if not selected_department:
    st.warning("Please select a department from the sidebar ⚠️")
    st.stop()
filtered_df = filtered_df[filtered_df['Department'].isin(selected_department)]

# Sidebar filter: Monthly Income Range
min_income = int(df['MonthlyIncome'].min())
max_income = int(df['MonthlyIncome'].max())
income_range = st.sidebar.slider("Select Monthly Income Range 💰", min_income, max_income, (min_income, max_income))
filtered_df = filtered_df[(filtered_df['MonthlyIncome'] >= income_range[0]) & (filtered_df['MonthlyIncome'] <= income_range[1])]

# Sidebar filter: Job Satisfaction Level
satisfaction_levels = sorted(df['JobSatisfaction'].unique().tolist())
selected_satisfaction = st.sidebar.multiselect("Select Job Satisfaction Levels 😊", satisfaction_levels, default=satisfaction_levels)
if not selected_satisfaction:
    st.warning("Please select a job satisfaction level from the sidebar ⚠️")
    st.stop()
filtered_df = filtered_df[filtered_df['JobSatisfaction'].isin(selected_satisfaction)]

# Displaying the Attrition Analysis header
st.header("Attrition Analysis 📊")

# Dropdown to select the type of visualization
visualization_option = st.selectbox(
    "Select Visualization 🎨", 
    ["Attrition by Age Group", 
     "KDE Plot: Distance from Home by Attrition", 
     "Attrition by Job Role", 
     "Attrition Distribution by Gender", 
     "MonthlyRate and DailyRate by JobLevel"]
)

# Visualizations based on user selection
if visualization_option == "Attrition by Age Group":
    # Bar chart for attrition by age group
    chart = alt.Chart(filtered_df).mark_bar().encode(
        x='AgeGroup',
        y='count()',
        color='Attrition'
    ).properties(
        title='Attrition Rate by Age Group'
    )
    st.altair_chart(chart, use_container_width=True)

elif visualization_option == "KDE Plot: Distance from Home by Attrition":
    # KDE plot for Distance from Home based on Attrition
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=filtered_df, x='DistanceFromHome', hue='Attrition', fill=True, palette='Set2')
    plt.xlabel('Distance From Home')
    plt.ylabel('Density')
    plt.title('KDE Plot of Distance From Home by Attrition')
    st.pyplot(plt)

elif visualization_option == "Attrition by Job Role":
    # Bar chart for attrition by job role
    chart = alt.Chart(filtered_df).mark_bar().encode(
        y='JobRole',
        x='count()',
        color='Attrition'
    ).properties(
        title='Attrition by Job Role'
    )
    st.altair_chart(chart, use_container_width=True)

elif visualization_option == "Attrition Distribution by Gender":
    # Pie chart for attrition distribution by gender
    pie_chart_data = filtered_df[filtered_df['Attrition'] == 'Yes']['Gender'].value_counts().reset_index()
    pie_chart_data.columns = ['Gender', 'count']
    
    chart = alt.Chart(pie_chart_data).mark_arc().encode(
        theta='count:Q',
        color='Gender:N',
        tooltip=['Gender', 'count']
    ).properties(
        title='Attrition Distribution by Gender',
        width=300,
        height=300
    ).project('identity')
    st.altair_chart(chart, use_container_width=True)

elif visualization_option == "MonthlyRate and DailyRate by JobLevel":
    # Boxplots for MonthlyRate and DailyRate by JobLevel
    fig, ax = plt.subplots(1, 2, figsize=(15, 7))
    
    # MonthlyRate by JobLevel
    sns.boxplot(x="JobLevel", y="MonthlyRate", data=filtered_df, ax=ax[0], palette='Set2')
    ax[0].set_title('MonthlyRate by JobLevel')
    ax[0].set_xlabel('Job Level')
    ax[0].set_ylabel('Monthly Rate')

    # DailyRate by JobLevel
    sns.boxplot(x="JobLevel", y="DailyRate", data=filtered_df, ax=ax[1], palette='Set2')
    ax[1].set_title('DailyRate by JobLevel')
    ax[1].set_xlabel('Job Level')
    ax[1].set_ylabel('Daily Rate')
    
    plt.tight_layout()
    st.pyplot(fig)

# Display dataset overview
st.header("Dataset Overview")
st.dataframe(df.describe())


# Insights from Visualization Section Expander
with st.expander("Insights from Visualization 🧠"):
    st.markdown("""
    1. **Age Groups & Attrition** - The 'Attrition by Age Group' plot showcases which age brackets face higher attrition.
    2. **Home Distance's Impact** - The 'KDE Plot: Distance from Home by Attrition' visualizes if being farther away influences leaving tendencies.
    3. **Roles & Attrition** - 'Attrition by Job Role' reveals which roles might be more attrition-prone.
    4. **Gender & Attrition** - The pie chart for 'Attrition Distribution by Gender' provides insights into any gender-based patterns.
    5. **Earnings Patterns** - 'MonthlyRate and DailyRate by JobLevel' boxplots display the compensation distribution across job levels.
    """)

# Recommendations Expander
with st.expander("Recommendations for Action 🌟"):
    st.markdown("""
    - 🎁 **Incentive Programs:** Introduce incentives tailored for groups showing higher attrition tendencies.
    - 🏡 **Remote Work Options:** Providing flexibility, especially for those living farther from the workplace, could reduce attrition.
    - 🚀 **Training & Growth:** Invest in employee development, especially in roles with higher attrition rates.
    - 👫 **Gender Equality:** Foster an environment that supports equal opportunities regardless of gender.
    - 💸 **Compensation Review:** Regularly review and adjust compensation structures to stay competitive and retain talent.
    """)
