from resources.anwb_api import api 


class parser:

    def __init__(self, road_of_interest, activities_of_interest):

        api_obj = api()
        self.response = api_obj.api()

        self.road_of_interest = road_of_interest
        self.activities_of_interest = activities_of_interest

    
    def parse_response(self):

        response_dt = self.response["dateTime"]
        print(response_dt)

        roads = self.response["roads"]

        for road in roads:

            if road["road"] == self.road_of_interest:

                segments = road["segments"]

                activity_dict = {}

                for segment in segments:

                    segment_info = f"{segment['start']} --> {segment['end']}"
                    interesting_things = dict(segment).keys()
                    interesting_thing = [thing for thing in interesting_things if thing in self.activities_of_interest]
                    for activities_of_interest in interesting_thing:
                        segment_all_activites = segment[activities_of_interest]
                        activity_dict[segment_info] = segment_all_activites
        
        return activity_dict
               