import requests
import streamlit as st

API_KEY = st.secrets["API_KEY"]


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_of_hours = 8 * forecast_days
    filtered_data = filtered_data[:no_of_hours]

    return filtered_data


if __name__ == "__main__":
    print(get_data("Pune", 2))
