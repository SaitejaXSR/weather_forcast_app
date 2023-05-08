import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Slide to increase number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dicti["main"]["temp"] / 10 for dicti in filtered_data]
        dates = [dicti["dt_txt"] for dicti in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        filtered_data = [dicti["weather"][0]["main"] for dicti in filtered_data]
        images_dict = {"Clear": "sky_images/clear.png", "Clouds": "sky_images/cloud.png",
                       "Rain": "sky_images/rain.png", "Snow": "sky_images/snow.png"}
        st.image([images_dict[image] for image in filtered_data], width=115)


