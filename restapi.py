import requests
import json
response = requests.get('http://stworzymy.pl/')

response.status_code
adam = response.text
print(adam)