import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

st.set_page_config(layout="wide")
df = pd.read_csv("India_mini_project.csv")

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Over-All-India')



st.sidebar.title("India few parameter visualization")

select_state = st.sidebar.selectbox("Select state",list_of_states)
select_primary_parameter = st.sidebar.selectbox("Select Primary",sorted(df.columns[5:]))
select_secondary_parameter = st.sidebar.selectbox("Select secondary",sorted(df.columns[5:]))



plot = st.sidebar.button('pLot Graph')

if plot:
    st.text("Size represents primary parameter")
    st.text("Color represents secondary parameter")
    if select_state=="Over-All-India":
        #plot for india
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=select_primary_parameter,color=select_secondary_parameter,zoom=3,mapbox_style="carto-positron",size_max=20,hover_name="District")
        st.plotly_chart(fig,use_container_width= True)
    else:
        #plot for states
        state_df=df[df['State'] == select_state]

        fig = px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',size=select_primary_parameter,color=select_secondary_parameter,zoom=3,mapbox_style="carto-positron",size_max=20,hover_name="District")
        st.plotly_chart(fig,use_container_width= True)