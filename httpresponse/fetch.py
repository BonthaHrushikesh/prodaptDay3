#get -fetch a user

import requests
BASE_URL = "https://jsonplaceholder.typicode.com"

#get - fetch a user
response = requests.get(f"{BASE_URL}/users/1")
print(response.status_code)
print(response.json())

#post - create a new user
new_post = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
print(response.status_code)
print(response.json())

#put,patch - partial update a user
response = requests.patch
print(response.status_code)
print(response.json())