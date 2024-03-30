from resources.parse import parser
from resources.create_msg import create_msg

import sys

road_of_interest = sys.argv[len(sys.argv) -1]
activities_of_interest = ["jams", "radars", "roadworks"]

def main():

    parser_obj = parser(road_of_interest=road_of_interest,
                        activities_of_interest=activities_of_interest)
    activity_dict = parser_obj.parse_response()

    if len(activity_dict) == 0:
        print(f"No activities of interest at {road_of_interest} right now")
    else:
        msg_obj = create_msg(road_of_interest, activity_dict)
        msg = msg_obj.create_msg()

        print(msg)

main()


'''
Get newest received message via signal api:
curl -X GET -H "Content-Type: application/json" 'http://localhost:8080/v1/receive/{number} -d '{"number": "{sender_number}", "max_messages": "1"}'
Send message via signal api:
curl -X POST -H "Content-Type: application/json" 'http://localhost:8080/v2/send' -d '{"message": "{msg}", "number": "{n}", "recipients": ["{n}"]}' 
'''