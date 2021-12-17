
import requests
  
payload ={'Name': 12345} #transfer args
URL = "https://httpbin.org/get"
r = requests.get('https://httpbin.org/get', params=payload)

  
print(r.text)  #r.json gives array