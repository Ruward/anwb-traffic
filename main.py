from resources.parse import parser
from resources.create_msg import create_msg

road_of_interest = "A12"
activities_of_interest = ["jams", "radars", "roadworks"]

def main():

    parser_obj = parser(road_of_interest=road_of_interest,
                        activities_of_interest=activities_of_interest)
    activity_list = parser_obj.parse_response()

    if len(activity_list) == 0:
        print(f"No activities of interest at {road_of_interest} right now")
    else:
        msg_obj = create_msg(road_of_interest, activity_list)
        msg = msg_obj.create_msg()

        print(msg)

main()