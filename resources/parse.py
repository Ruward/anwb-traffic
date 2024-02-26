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

                for segment in segments:

                    interesting_things = dict(segment).keys()
                    interesting_thing = [thing for thing in interesting_things if thing in self.activities_of_interest]
                    print(interesting_thing)
                        