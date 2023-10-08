import requests

# Define the API endpoint and headers
url = 'https://services.sentinel-hub.com/api/v1/catalog/1.0.0/search'
headers = {
    'Authorization': 'Bearer <your access token>',
    'Content-Type': 'application/json',
}

# Define the request payload
payload = {
    "bbox": [13, 45, 14, 46],
    "datetime": "2019-12-10T00:00:00Z/2019-12-10T23:59:59Z",
    "collections": ["sentinel-1-grd"],
    "limit": 5
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    # Print the response content (JSON data)
    print(response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
