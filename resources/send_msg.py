import requests 

class sender:

    def __init__(self, ip: str, act: str, msg: str, road_of_interest: str, pwd: str):

        self.ip = ip
        self.act = act
        self.msg = msg
        self.road = road_of_interest
        self.pwd = pwd

    
    def send_jam(self, delay: str):

        url = f"http://{self.ip}/A12-verkeer"
        headers = {"Title": f"{self.act} on {self.road}, delay: {delay} minutes",
                   "Tags": "warning"}

        response = requests.post(url=url,
                                 headers=headers,
                                 auth=("ruward", self.pwd),
                                 data=self.msg)
        
        return response
    

    def send_radar(self):

        url = f"http://{self.ip}/A12-verkeer"
        headers = {"Title": f"{self.act} on {self.road}, watch speed",
                   "Tags": "warning"}

        response = requests.post(url=url,
                                 headers=headers,
                                 auth=("ruward", self.pwd),
                                 data=self.msg)
        
        return response