from resources.parse import parser
 
road_of_interest = "A12"
activities_of_interest = ["jams", "roadworks", "radars"]

def main():

    parser_obj = parser(road_of_interest=road_of_interest,
                        activities_of_interest=activities_of_interest)
    parser_obj.parse_response()

main()