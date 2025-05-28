import streamlit as st
import pandas as pd
import plotly.express as px
from dashboard_app.data_loader import load_data
from dashboard_app.utils import preprocess_data

st.set_page_config(page_title="Disaster Response Dashboard", layout="wide")

st.title("🌐 Real-Time Disaster Response Dashboard")

# Load and preprocess data
data = load_data("data/sample_data.csv")
df = preprocess_data(data)

# Sidebar filters
disaster_type = st.sidebar.multiselect("Select Disaster Type", df["Disaster Type"].unique())
if disaster_type:
    df = df[df["Disaster Type"].isin(disaster_type)]

# Map
st.subheader("Disaster Event Locations")
fig_map = px.scatter_mapbox(df,
                            lat="Latitude",
                            lon="Longitude",
                            color="Disaster Type",
                            zoom=2,
                            height=400,
                            hover_name="Location",
                            mapbox_style="carto-positron")
st.plotly_chart(fig_map, use_container_width=True)

# Stats
st.subheader("Event Frequency")
fig_bar = px.histogram(df, x="Disaster Type", color="Disaster Type", barmode="group")
st.plotly_chart(fig_bar, use_container_width=True)