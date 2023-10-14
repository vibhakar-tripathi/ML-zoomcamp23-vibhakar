import requests

url = "http://0.0.0.0:9669/predict"

client ={'job': 'unknown', 
 'duration': 270, 
 'poutcome': 'failure'}
response = requests.post(url,json=client).json()

print(response)
