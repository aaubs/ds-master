import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering

# Load your NBA data here
df = pd.read_csv('https://raw.githubusercontent.com/aaubs/ds-master/main/data/NBA_Data.csv')

# Preprocess and standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.select_dtypes(include=[np.number]))

# Perform clustering (k-means and hierarchical)
kmeans = KMeans(n_clusters=4).fit(scaled_data)
agg_clustering = AgglomerativeClustering(n_clusters=4).fit(scaled_data)

# Add cluster labels to the original DataFrame
df['KMeans_Cluster'] = kmeans.labels_
df['Agg_Cluster'] = agg_clustering.labels_

# Streamlit app
st.title("NBA Player Injury Replacement Recommender")

st.write("""
Select an injured player and get recommendations for replacement players based on playing style and statistics.
""")

# User selects an injured player
injured_player = st.selectbox("Select an Injured Player", df['PLAYER'].unique())

# Find the cluster of the injured player in both clustering models
injured_kmeans_cluster = df[df['PLAYER'] == injured_player]['KMeans_Cluster'].values[0]
injured_agg_cluster = df[df['PLAYER'] == injured_player]['Agg_Cluster'].values[0]

# Recommend replacement players from the same cluster
kmeans_replacements = df[df['KMeans_Cluster'] == injured_kmeans_cluster].sort_values(by='PTS', ascending=False).head(5)
agg_replacements = df[df['Agg_Cluster'] == injured_agg_cluster].sort_values(by='PTS', ascending=False).head(5)

st.write(f"### Recommendations based on K-means Clustering")
st.write(kmeans_replacements[['PLAYER', 'PTS', 'REB', 'AST']])

st.write(f"### Recommendations based on Hierarchical Clustering")
st.write(agg_replacements[['PLAYER', 'PTS', 'REB', 'AST']])
