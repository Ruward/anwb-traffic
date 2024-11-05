class create_msg:

    def __init__(self):

        print("init msg generation")


    def activity_msg(self, road_name: str, activity: dict, segment_start: str, segment_end: str) -> dict:

        str_dict = {}
        delay = ""

        if activity['road_name'] == road_name.upper().strip() and activity['segment_start'] == segment_start and activity['segment_end'] == segment_end:

            if activity['event_name'] == 'jams' and activity['incident'] != 'road-closed':
                key = activity['id']
                delay = str(int(activity['delay']/60))
                opening_string = f"Traffic jam on {road_name}: {activity['segment_start']} to {activity['segment_end']}."
                info_string = f"Jam starts at {activity['jam_start']}, ends at {activity['jam_end']}."
                end_string = f"{activity['incident']}: {activity['description']}, expected delay {delay} minutes"

                str_dict['type'] = 'jam'
                str_dict['key'] = key 
                str_dict['opening'] = opening_string
                str_dict['info'] = info_string
                str_dict['end'] = end_string
                
            elif activity['event_name'] == 'radars':
                key = activity['id']
                opening_string = f"Warning: radar detected on {road_name}: {activity['segment_start']} to {activity['segment_end']}."
                info_string = f"Radar located at HM {activity['location_hm']}."

                str_dict['type'] = 'radar'
                str_dict['key'] = key 
                str_dict['opening'] = opening_string
                str_dict['info'] = info_string
                str_dict['end'] = ''

        return str_dict, delay
        
    
    def create_msg(self, road_name: str, activity: dict, segment_start: str, segment_end: str) -> str:
        
        str_dict, delay = self.activity_msg(road_name, activity, segment_start, segment_end)

        try:
            msg = f"{str_dict['opening']}\n\n{str_dict['info']}\n\n{str_dict['end']}"
        except:
            return '', delay
        else:
            return msg, delay

