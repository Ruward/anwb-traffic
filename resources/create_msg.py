class create_msg:

    def __init__(self, road_of_interest, activity_dict: dict):

        self.road_of_interest = road_of_interest
        self.activity_dict = activity_dict
        self.init_str = f"This is the current traffic situation on {self.road_of_interest}:\n\n"
        self.close_str = f"\n\n Happy driving!"


    def activity_msg(self, activity):

        filler_strs = ''

        if activity['category'] == 'jams':

            filler_strs = [f"Type: {activity['category']}\n"
                        , f"Incident: {activity['incidentType']}\n"
                        , f"From location: {activity['from']}\n"
                        , f"To location: {activity['to']}\n"
                        , f"Delay: {activity['delay']}\n"
                        , f"Start time: {activity['start']}\n"
                        , f"Explanation: {activity['reason']}\n\n"
            ] 


        if activity['category'] == 'roadworks':

            filler_strs = [f"Type: {activity['category']}\n"
                        , f"Incident: {activity['incidentType']}\n"
                        , f"From location: {activity['from']}\n"
                        , f"To location: {activity['to']}\n"
                        , f"From date: {activity['start']}\n"
                        , f"To date: {activity['stop']}\n"
                        , f"Explanation: {activity['reason']}\n\n"
            ]            

        
        if activity['category'] == 'radars':
            
            filler_strs = [f"Type: {activity['category']}\n"
                        , f"Incident: {activity['incidentType']}\n"
                        , f"From location: {activity['from']}\n"
                        , f"To location: {activity['to']}\n"
                        , f"Hectometerpaal: {activity['HM']}\n"
                        , f"Explanation: {activity['events'][0]['text']}\n\n"
                        ]

        return filler_strs
        
    
    def create_msg(self):
        
        total_str = ""

        for segment, activities in self.activity_dict.items():

            start_str = f"{segment}\n\n"
            total_str += start_str
            for segment_activities in activities:
                for activity in segment_activities:
                    filler_strs = self.activity_msg(activity)
                    for str in filler_strs:
                        total_str += str
        
        final_str = self.init_str + total_str + self.close_str

        return final_str
