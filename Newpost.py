import requests
import json

test_file = open("1.py", "rb")
test_url = "http://httpbin.org/post"
test_response = requests.post(test_url, files = {"form_field_name": test_file})


if test_response.ok:
    print("Post completed")
    print(test_response.text)
else:
    print("Error")