import requests
from requests.exceptions import HTTPError

def get_api_response(url, params):
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
    except HTTPError as http_err:
        print(f'A HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'An error occurred: {err}') 
    else:
        return resp.json()