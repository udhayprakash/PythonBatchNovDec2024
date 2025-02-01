import requests
from pprint import pp

url = 'http://127.0.0.1:8080'
response = requests.get(url)
pp(dict(response.headers))

print(response.headers[ 'Content-Type'])

print(response.text)  # Hello, World!
