import json
import requests
from pprint import pprint


def postcode_output(postcode_input):
    json_body = json.dumps({"postcodes": [postcode_input]})
    headers = {"content-Type": "application/json"}
    post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)
    print(post_multi_req.status_code)
    pprint(post_multi_req.json())


postcode_input = input("What postcode would you like to look up? \n")
postcode_input = postcode_input.replace(" ", "")
print(postcode_input)
postcode_output(postcode_input)
