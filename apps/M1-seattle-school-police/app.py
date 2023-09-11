import streamlit as st
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Load the datasets
@st.cache_data
def load_data():
    police = pd.read_csv('https://raw.githubusercontent.com/aaubs/ds-master/main/data/geopandas_data/SPD_Officer_Involved_Shooting__OIS__Data.csv')
    gdf_ps = gpd.read_file('https://raw.githubusercontent.com/aaubs/ds-master/main/data/Public_Schools.geojson')
    gdf = gpd.read_file('https://raw.githubusercontent.com/aaubs/ds-master/main/data/geopandas_data/Neighborhood_Map_Atlas_Districts.geojson')
    return police, gdf_ps, gdf

police, gdf_ps, gdf = load_data()

st.title("Police Involved Shooting and School Data Analysis in Seattle 🚔🏫")

st.markdown("""
            This dashboard provides insights into police-involved shootings and school data in Seattle. Explore different analyses using the menu below.
""")

analysis_option = st.selectbox(
    "Select Analysis 📈",
    ["Spatial Distribution of Data",
     "Common Neighborhoods for Police-Involved Shootings",
     "Neighborhoods Without Police-Involved Shootings",
     "Schools Near Shooting Locations",
     "Type of Schools Near Shootings",
     "Schools Without Police-Involved Shootings",
     "School with Most Shootings"]
)

gdf_police = gpd.GeoDataFrame(police, geometry=gpd.points_from_xy(police['Longitude'], police['Latitude']))
gdf_police.crs = "EPSG:4326"

# Update CRS
gdf_police = gdf_police.to_crs("EPSG:4326")
gdf = gdf.to_crs("EPSG:4326")
gdf_ps = gdf_ps.to_crs("EPSG:4326")

# Join operations outside the if-else for shared use
joined_police_gdf = gpd.sjoin(gdf_police, gdf, how="left", predicate="within")
joined_police_ps = gdf_police.sjoin_nearest(gdf_ps, how='left')

if analysis_option == "Spatial Distribution of Data":
    st.subheader("Spatial Distribution of Police Shootings, Public Schools and Neighborhoods")
    
    m = folium.Map(location=[47.6062, -122.3321], zoom_start=11, tiles="CartoDB positron")

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(m)

    # Loop through each police shooting and add it as a circle on the map within the marker cluster
    for _, row in gdf_police.iterrows():
        # Creating a pop-up message with some key information about the incident
        popup_content = f"""
        Incident Number: {row['Incident Number']}<br>
        Date/Time: {row['Date / Time']}<br>
        Address: {row['Blurred Address']}<br>
        Officer Rank: {row['Rank']}<br>
        Officer Gender: {row['Officer Gender']}<br>
        Subject Gender: {row['Subject Gender']}<br>
        Subject Race: {row['Subject Race']}<br>
        """
        popup = folium.Popup(popup_content, max_width=300)
        
        folium.Circle(
            location=[row['Latitude'], row['Longitude']],
            radius=15,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.4,
            popup=popup
        ).add_to(marker_cluster)

    st_folium(m)


elif analysis_option == "Common Neighborhoods for Police-Involved Shootings":
    st.subheader("Common Neighborhoods for Police-Involved Shootings")
    counts = joined_police_gdf.L_HOOD.value_counts()
    st.table(counts)

elif analysis_option == "Neighborhoods Without Police-Involved Shootings":
    st.subheader("Neighborhoods Without Police-Involved Shootings")
    no_shooting_neighborhoods = gdf[~gdf.L_HOOD.isin(joined_police_gdf.L_HOOD.unique().tolist())]
    
    m = folium.Map(location=[47.6062, -122.3321], zoom_start=11, tiles="CartoDB positron")
    no_shooting_neighborhoods = no_shooting_neighborhoods.to_crs(epsg=4326)
    for _, r in no_shooting_neighborhoods.iterrows():
        sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillColor": "orange"})
        folium.Popup(r["L_HOOD"]).add_to(geo_j)
        geo_j.add_to(m)

    st_folium(m)

elif analysis_option == "Schools Near Shooting Locations":
    st.subheader("Schools Near Shooting Locations")
    joined_police_ps = gdf_police.sjoin_nearest(gdf_ps, how='left')
    school_counts = joined_police_ps.NAME.value_counts()
    st.table(school_counts)

elif analysis_option == "Type of Schools Near Shootings":
    st.subheader("Type of Schools Near Shootings")
    type_counts = joined_police_ps.TYPE.value_counts()
    st.table(type_counts)

elif analysis_option == "Schools Without Police-Involved Shootings":
    st.subheader("Schools Without Police-Involved Shootings")
    schools_without_shootings = gdf_ps[~gdf_ps.NAME.isin(joined_police_ps.NAME.unique().tolist())]
    schools_without_shootings = schools_without_shootings.to_crs(epsg=4326)
    m = folium.Map(location=[47.6062, -122.3321], zoom_start=11, tiles="CartoDB positron")

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(m)

    # Loop through each school and add it as a circle on the map within the marker cluster
    for _, row in schools_without_shootings.iterrows():
        folium.Circle(
            location=[row.geometry.y, row.geometry.x],
            radius=20,  # you can adjust the radius
            color='violet',
            fill=True,
            fill_color='violet',
            fill_opacity=0.6,
            popup=row['SCHOOL']
        ).add_to(marker_cluster)
    st_folium(m)

elif analysis_option == "School with Most Shootings":
    st.subheader("School with Most Police-Involved Shootings")
    joined_police_ps_max = gdf_police.sjoin_nearest(gdf_ps, how='left', max_distance=0.09, distance_col="distances")
    max_shooting_school = joined_police_ps_max.groupby(['NAME'])[['distances', 'NAME']].agg({'distances': 'mean', 'NAME': 'count'})
    st.table(max_shooting_school)

# Plotting shootings by subject's race
st.subheader("Shootings by Subject's Race")
subject_race = gdf_police['Subject Race'].value_counts()
st.bar_chart(subject_race)