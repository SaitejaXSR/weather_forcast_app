import requests

API_KEY = "db4b6184e00d17fc97c23cb2f1e2cfe9"


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
