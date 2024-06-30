import requests 
import os 
from dotenv import load_dotenv

class api:

    def __init__(self):

        load_dotenv() 

        self.api_key = os.getenv("api_key")
    

    def api(self):

        url = f"https://api.anwb.nl/v2/incidents/desktop?apikey={self.api_key}"
        headers = {"Content-Type": "application/json"}

        response = requests.get(url=url, headers=headers)
        response = response.json()

        return response
