import requests 

class api:

    def __init__(self):

        self.api_key = "8VzRhyPujV01WvpTwnUJucejIXMt5eht"
    

    def api(self):

        url = f"https://api.anwb.nl/v2/incidents/desktop?apikey={self.api_key}"
        headers = {"Content-Type": "application/json"}

        response = requests.get(url=url, headers=headers)
        response = response.json()

        return response
