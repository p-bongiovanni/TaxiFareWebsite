import streamlit as st
import datetime
import requests

url = 'https://taxifare.lewagon.ai/predict'

'''
# TaxiFareModel front
'''



pickup_date = st.date_input(
    "Pickup Date",
    datetime.date(2019, 7, 6))
pickup_time = st.time_input('Pickup time', datetime.time(8, 45))
pickup_datetime = datetime.datetime.combine(pickup_date,
                          pickup_time)

p_long = st.number_input('Insert the pickup the Longitude๐')

st.write('pick up long is ', p_long)


p_lat = st.number_input('Insert the pickup a Latidude๐')

st.write('pick up lat is ', p_lat)



d_long = st.number_input('Insert the pickup the Longitude๐ฆผ')

st.write('drop out long is ', d_long)


d_lat = st.number_input('Insert the pickup a Latidude๐')

st.write('drop out lat is ', d_lat)

number = st.number_input('Insert the numbers of passagenrs ๐ฉ๐ฟโ๐คโ๐ง๐ฟ๐ฉ๐ฟโ๐คโ๐ง๐ฟ๐ฉ๐พโ๐คโ๐ง๐ป๐ฉ๐ฟโ๐คโ๐ง๐ฝ๐จ๐พโ๐คโ๐จ๐ป', step=1)


st.write('number of ppl are ', number)

if number != 0:

    url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={pickup_datetime}&pickup_longitude={p_long}&pickup_latitude={p_lat}&dropoff_longitude={d_long}&dropoff_latitude={d_lat}&passenger_count={number}'
    st.write(url)
    response = requests.get(
        url,
    ).json()

    st.success(f'cum, {response}')
