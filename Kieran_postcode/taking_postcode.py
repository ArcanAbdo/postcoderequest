import json
import requests


def post_code_query():
    postcode = input('What postcode would you like to search? ')

    if 4 < len(postcode) < 9:
        try:
            post_code_req = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
            return post_code_req.json()
        finally:
            print('Execution complete')
    else:
        print('Sorry check postcode length and try again!')
        post_code_query()


post_code_query()
