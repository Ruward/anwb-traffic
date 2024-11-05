import requests 
import json
import os

from dotenv import load_dotenv 


def listen(ntfy_pwd: str) -> None: 

    pwd = ntfy_pwd

    dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir)
    
    with open("programs.json", "r") as file:
        config = json.loads(file.read())
        file.close() 

    response = requests.get(url='http://ntfy-server/A12-verkeer/json', 
                            auth=("ruward", pwd), 
                            stream=True)

    for line in response.iter_lines():
        print(line)
        line = line.decode('utf8').replace("'", '"')
        line = json.loads(line)

        if line and 'message' in line.keys():
            if line['message'] == '1':
                anwb_from = config['programs']['1']['start']
                anwb_to = config['programs']['1']['to']
                anwb_road = config['programs']['1']['road']
            elif line['message'] == '2':
                anwb_from = config['programs']['2']['start']
                anwb_to = config['programs']['2']['to']
                anwb_road = config['programs']['2']['road']
            else:
                anwb_from = ""
                anwb_to = ""
                anwb_road = "" 

            body = {'road': anwb_road, 'segment_start': anwb_from, 'segment_end': anwb_to}
            body = json.dumps(body)
        
            requests.post(url='http://anwb-notifier:7000/traffic',
                            headers={'content-type': 'application/json', 'key': os.getenv('flask_key')},
                            data=body)
            break

if __name__ == '__main__':
    load_dotenv() 
    pwd = os.getenv('ntfy_pwd')

    listen(pwd)