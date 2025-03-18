#Liabraryies
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

#Time Zone
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

#Title
st.title("Time Zone App")

#Select Box
select_timezone = st.multiselect("Select Timezones", TIME_ZONES , default=["UTC","Asia/Karachi"])

#selected timezone
st.subheader("Selected Timezones")
for tz in select_timezone:
    
    #Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    #display the current time for each selected timezone
    st.write(f"**{tz}**: {current_time}")
    
#Create a subheader for converting time between timezones   
st.subheader("Convert Time Between Timezones")

#Create a time input widge for the current time
current_time = st.time_input("Current Time", value=datetime.now().time())

#create a selectbox for selecting the timezone to convert from
from_tz = st.selectbox("From Timezone", TIME_ZONES , index=0)

#create a selectbox for selecting the timezone to convert to
to_tz = st.selectbox("To Timezone", TIME_ZONES , index=1)

#Create a button to convert the time
if st.button("Convert Time"):

    #combine the current time and the selected timezones
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    
    #convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
    #Display the converted time
    st.success(f"Converted Time in {to_tz}: {converted_time}")

