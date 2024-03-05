class create_msg:

    def __init__(self, road_of_interest, activity_list):

        self.road_of_interest = road_of_interest
        self.activity_list = activity_list
        self.init_str = f"This is the current traffic situation on {self.road_of_interest}:\n\n"
        self.close_str = f"\n\n Happy driving!"


    def activity_msg(self, activity):

        filler_strs = [f"Type: {activity['category']}\n"
                       , f"Incident: {activity['incidentType']}\n"
                       , f"From location: {activity['from']}\n"
                       , f"To location: {activity['to']}\n"
                       , f"From date: {activity['start']}\n"
                       , f"To date: {activity['stop']}\n"
                       , f"Explanation: {activity['reason']}\n\n"
        ]            

        return filler_strs
        
    
    def create_msg(self):
        
        total_str = ""

        for activity in self.activity_list:
            filler_strs = self.activity_msg(activity)
            for str in filler_strs:
                total_str += str
        
        final_str = self.init_str + total_str + self.close_str

        return final_str
