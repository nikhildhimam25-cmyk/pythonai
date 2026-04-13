


# API_KEY = "lPRp8eAboomzzrC7FdhmsHUgTHq3ttdIDfUsLIpf"

# import requests

# url = "https://api.nasa.gov/planetary/apod"
# params = {
#     "api_key": API_KEY
# }

# response = requests.get(url, params=params)
# print(response.json())

import requests
import requests

API_KEY = "579b464db66ec23bdd0000012a80caaf0a904ced5df21ba93f0e1cb2"
RESOURCE_ID = "/resource/1903f3ef-f74d-4b00-adc0-b74f5c7e0d92"

def get_data():
    url = f"https://api.data.gov.in/resource/"

    params = {
        "api-key": API_KEY,
        "format": "json",
        "limit": 10
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    return None
if __name__=="__main__":
  get_data()
