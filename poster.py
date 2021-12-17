import requests

  
payload ={'username': 'cem',} #post args
URL = "https://httpbin.org/post"
r = requests.post('https://httpbin.org/post', data=payload)

#r_dict = r.json()  

print(r.text)