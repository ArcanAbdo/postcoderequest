import requests
import json
from pprint import pprint


def post_code_info(postcode):
    post_code_req = requests.get("http://api.postcodes.io/postcodes/" + postcode)
    return "Country: " + post_code_req.json()['result']['country'],\
           "Region: " + post_code_req.json()['result']['region'],\
           "County: " + post_code_req.json()['result']['admin_county'],\
           "Local District: " + post_code_req.json()['result']['admin_district']