import requests
import json

#the url where we send the request to

webhook_url = 'https://enfhzl41ugwinhs.m.pipedream.net'

data = { 'study_id': 123,
        'flow_id_1': 2332,
        'flow_id_2': 23211,
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'type':'jsonwhat'})
