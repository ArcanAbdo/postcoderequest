import json
import requests


# Class definition
class PostCode:

    # Initialisation of postcode
    def __init__(self, postcode):
        self.postcode = postcode

    # Determines if the entered postcode has a valid length.
    def check_length(self):

        if 6 <= len(self.postcode) <= 8:
            try:
                post_code_req = requests.get(f"https://api.postcodes.io/postcodes/{self.postcode}")
            finally:
                return 'Postcode length is valid'
        else:
            print('Sorry check postcode length and try again!')

    # Returns the postcode details in full.
    def output_full(self):
        json_body = json.dumps({"postcodes": [self.postcode]})
        headers = {"content-Type": "application/json"}
        post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)
        print(type(post_multi_req.json()))
        return post_multi_req.json()

    # Returns the postcode details relating to its location.
    def output_location(self):
        post_code_req = requests.get("http://api.postcodes.io/postcodes/" + self.postcode)
        try:
            return "Country: " + str(post_code_req.json()['result']['country']), \
                   "Region: " + str(post_code_req.json()['result']['region']), \
                   "Local District: " + str(post_code_req.json()['result']['admin_district']), \
                   "County: " + str(post_code_req.json()['result']['admin_county'])
        except KeyError:
            print("Post code doesn't exist.")
