import requests

response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 16.8409,
    'lng': 96.1735,
    'params': 'pressure',
  },
  headers={
    'Authorization': '9da1e6bc-4736-11ee-8b7f-0242ac130002-9da1e78e-4736-11ee-8b7f-0242ac130002'
  }
)

# Do something with response data.
json_data = response.json()
print(json_data)