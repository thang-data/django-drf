import requests

# endpoint ='https://httpbin.org/status/200'
endpoint = 'http://localhost:1323/api'

get_response = requests.get(endpoint, json={
    "query": "Hello world"
})

# print(get_response.text)
# print(get_response.json())
print(get_response.status_code)
