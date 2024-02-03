import requests

# API endpoint URL
api_url = "https://api.thaistock2d.com/live"

try:
    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        json_data = response.json()

        # Extract 2D values from the "result" list
        twod_values = [entry["twod"] for entry in json_data["result"]]

        print("2D Lottery Numbers:", twod_values)
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
