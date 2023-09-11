# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the Seaborn style to 'ggplot'
sns.set(style="whitegrid", palette="pastel", color_codes=True)


# Function to load the dataset
@st.cache_data  # Cache the function to enhance performance
def load_data():
    # Define the file path
    file_path = 'https://sds-aau.github.io/SDS-master/M1/data/RI-clean.csv.gz'
    
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv(file_path, low_memory=False)

    # Handle missing and irrelevant columns
    df.drop(['id', 'state', 'county_name', 'county_fips', 'fine_grained_location'], axis='columns', inplace=True)
    df.dropna(subset=['stop_date', 'stop_time', 'driver_gender'], inplace=True)

    # Convert to proper data types and create datetime index
    df['is_arrested'] = df['is_arrested'].astype('bool')
    df['search_conducted'] = df['search_conducted'].astype('bool')
    df['datetime'] = pd.to_datetime(df['stop_date'] + ' ' + df['stop_time'])
    df.set_index('datetime', inplace=True)

        # Handle missing values
    df['out_of_state'].fillna(df['out_of_state'].mode()[0], inplace=True)
    df[['driver_age', 'driver_age_raw']].fillna(df[['driver_age', 'driver_age_raw']].median(), inplace=True)

    bins = pd.IntervalIndex.from_tuples([(10, 20), (20, 30), (30, 40), (40, 50), (50, 100)])

    # Create age categories
    labels = ["teen", "20s", "30s", "40s", "50+"]
    bins = pd.IntervalIndex.from_tuples([(10, 20), (20, 30), (30, 40), (40, 50), (50, 100)])
    df['age_cat'] = pd.cut(df.driver_age, bins=bins)

    return df

# Load the data using the defined function
df = load_data()


selected_age_group = st.multiselect("Select Age Groups 🕰️", df['age_cat'].unique().tolist(), default=df['age_cat'].unique().tolist())
if not selected_age_group:
    st.warning("Please select an age group from the sidebar ⚠️")
    st.stop()
filtered_df = df[df['age_cat'].isin(selected_age_group)]


# Theme 1: Demographic Disparities in Traffic Stops
## Distribution of driver genders and races among the traffic stops
gender_distribution = filtered_df['driver_gender'].value_counts(normalize=True) * 100
race_distribution = filtered_df['driver_race'].value_counts(normalize=True) * 100


st.title("Rhode Island Traffic Stops Dashboard 🚗🚓")


st.dataframe(gender_distribution)

st.dataframe(race_distribution)