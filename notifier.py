from resources.anwb_api import api
from resources.api_parser import api_parser
#from resources.dao import DAO
from resources.create_msg import create_jam_msg, create_radar_msg
from resources.send_msg import sender

import sys
import os
from dotenv import load_dotenv


def main(road_of_interest: str, segment_start: str, segment_end: str):

  load_dotenv()

  ntfy_pwd = os.getenv("ntfy_pwd")
  ntfy_ip = os.getenv("ntfy_ip")

  road_of_interest = road_of_interest.upper()

  api_obj = api()
  response = api_obj.api()

  rw_list, ja_list, rd_list = api_parser(response).parse_response()
  
#  resp = DAO(rw_list, ja_list, rd_list).insert_data()
#  print(resp)

  jams = False 
  radars = False 

  if len(ja_list) > 0:
    jam_msg, delay = create_jam_msg().create_msg(road_of_interest, ja_list, segment_start, segment_end)
    
    if len(jam_msg) > 0:
      jams = True 
      act = "Jam(s)"
      sender(ntfy_ip, act, jam_msg, road_of_interest, ntfy_pwd).send_jam(delay)
  
  if len(rd_list) > 0:
    radar_msg, delay = create_radar_msg().create_msg(road_of_interest, rd_list, segment_start, segment_end)

    if len(radar_msg) > 0:
      radars = True
      act = "Radar(s)"
      sender(ntfy_ip, act, radar_msg, road_of_interest, ntfy_pwd).send_radar()

  if not jams and not radars:
    act = "All clear"
    msg = f"Currently no jams or radars on {road_of_interest}"
    delay = "0"
    sender(ntfy_ip, act, msg, road_of_interest, ntfy_pwd).send_jam(delay)


if __name__ == "__main__":
  road_of_interest = sys.argv[len(sys.argv) - 3]
  segment_start = sys.argv[len(sys.argv)- 2]
  segment_end = sys.argv[len(sys.argv) - 1]
  main(road_of_interest, segment_start, segment_end)
