from resources.parse import parser
from resources.create_msg import create_msg

import sys

def main(road_of_interest):

    activities_of_interest = ["jams", "radars", "roadworks"]

    parser_obj = parser(road_of_interest=road_of_interest,
                        activities_of_interest=activities_of_interest)
    activity_dict = parser_obj.parse_response()

    if len(activity_dict) == 0:
        print(f"No activities of interest at {road_of_interest} right now")
    else:
        msg_obj = create_msg(road_of_interest, activity_dict)
        response_dict = msg_obj.create_msg()
        return response_dict


if __name__ == "__main__":
    road_of_interest = sys.argv[len(sys.argv)-1]
    main(road_of_interest)

