class create_msg:

    def __init__(self, road_of_interest, activity_dict: dict):

        self.road_of_interest = road_of_interest
        self.activity_dict = activity_dict
        self.response_dict = {}
        self.init_str = f"{self.road_of_interest}"
        self.close_str = f"Happy driving!"


    def activity_msg(self, activity_list):

        str_dict = {}
        for activity in activity_list:

            if activity['category'] == 'jams':
                
                key = activity['id']
                filler_strs = {"Type": activity['category']
                            , "Incident": activity['incidentType']
                            , "From location": activity['from']
                            , "To location": activity['to']
                            , "Delay": activity['delay']
                            , "Start time": activity['start']
                            , "Explanation": activity['reason']
                } 

                str_dict[key] = filler_strs


            if activity['category'] == 'roadworks':

                key = activity['id']
                filler_strs = {"Type": activity['category']
                            , "Incident": activity['incidentType']
                            , "From location": activity['from']
                            , "To location": activity['to']
                            , "From date": activity['start']
                            , "To date": activity['stop']
                            , "Explanation": activity['reason']
                }           
                
                str_dict[key] = filler_strs
        
            if activity['category'] == 'radars':
                
                key = activity['id']
                filler_strs = {"Type": activity['category']
                            , "Incident": activity['incidentType']
                            , "From location": activity['from']
                            , "To location": activity['to']
                            , "Hectometerpaal": activity['HM']
                            , "Explanation": activity['events'][0]['text']
                }

                str_dict[key] = filler_strs

        return str_dict
        
    
    def create_msg(self):
        
        segment_dict = {}
        for segment, activities in self.activity_dict.items():

            for segment_activities in activities:
  
                str_dict = self.activity_msg(segment_activities)
            
            segment_dict[segment] = str_dict
        
        self.response_dict[self.init_str] = segment_dict

        return self.response_dict
