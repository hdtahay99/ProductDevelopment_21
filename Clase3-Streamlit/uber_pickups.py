import math

import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Uber pickups test")

DATA_SOURCE = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"

@st.cache(allow_output_mutation=True)
def download_data():
    return (pd.read_csv(DATA_SOURCE)).rename(columns={'Lat':'lat', 'Lon':'lon'})

df = download_data()
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

start_hour, end_hour = st.slider('Select the time interval ',0, 24, (10, 12))

data = df[df['Date/Time'].dt.hour.between(start_hour, end_hour)]

page_size = 1000

total_pages = math.ceil(len(data) / page_size)

page = st.slider('Select the page data ', 1, total_pages, (1))

start_idx = (page - 1) * page_size
end_idx   = page * page_size

sub_data = data.iloc[start_idx:end_idx]

"""
### List Uber Pickups With Filters
"""
st.write(sub_data)

"""
### Map Uber Pickups With Filters
"""
st.map(sub_data)

"""
### Number of uber pickups per hour
"""

temp = data.copy()

temp['Number per hour'] = data['Date/Time'].dt.hour

temp = temp['Number per hour'].value_counts()

st.bar_chart(temp)


