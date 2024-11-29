class create_jam_msg:

    def __init__(self):

        print("Init jam msg generation")


    def gather_activities(self, road_name: str, activity_list: list, segment_start: str, segment_end: str) -> dict:

        jam_list = []

        for activity in activity_list:

            if activity['road_name'] == road_name.upper().strip() and activity['segment_start'] == segment_start and activity['segment_end'] == segment_end:
                if activity['event_name'] == 'jams' and activity['incident'] != 'road-closed':
                    jam_list.append(activity)

        return jam_list
    

    def construct_jam(self, road_name: str, jam_list: list):

        str_dict = {}
        delay = ""

        if len(jam_list) == 1: 
            activity = jam_list[0]
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

        elif len(jam_list) > 1:
            activity = jam_list[0]
            opening_string = f"Multiple traffic jams on {road_name}: {activity['segment_start']} to {activity['segment_end']}."
            start_end_list = []
            delay_list = []
            surr_key = []
            
            for activity in jam_list:
                key = activity['id']
                surr_key.append(key)
                delay = str(int(activity['delay']/60))
                
                info_string = f"{activity['jam_start']} to {activity['jam_end']}: {activity['incident']}, {activity['description']}, expected delay {delay} minutes"
                start_end_list.append(info_string)
                delay_list.append(int(delay))
                
            surrogate_key = "-".join(str(surr_key))
            total_info = "\n".join(start_end_list)
            delay = sum(delay_list)
            end_string = f"Total expected delay {delay} minutes"

            str_dict['type'] = 'jam'
            str_dict['key'] = surrogate_key 
            str_dict['opening'] = opening_string
            str_dict['info'] = total_info
            str_dict['end'] = end_string

        return str_dict, delay
        
    
    def create_msg(self, road_name: str, activity_list: list, segment_start: str, segment_end: str) -> str:

        jam_list = self.gather_activities(road_name, activity_list, segment_start, segment_end)

        jam_str_dict, jam_delay = self.construct_jam(road_name, jam_list)

        if len(jam_str_dict) > 0: 
            jam_msg = f"{jam_str_dict['opening']}\n\n{jam_str_dict['info']}\n\n{jam_str_dict['end']}"
        else: 
            jam_msg = ''
            
        return jam_msg, jam_delay


class create_radar_msg: 

    def __init__(self):

        print("Init radar msg generation")


    def gather_activities(self, road_name: str, activity_list: list, segment_start: str, segment_end: str) -> dict:

        radar_list = []

        for activity in activity_list:

            if activity['road_name'] == road_name.upper().strip() and activity['segment_start'] == segment_start and activity['segment_end'] == segment_end:       
                if activity['event_name'] == 'radars':
                    radar_list.append(activity)

        return radar_list
    

    def construct_radar(self, road_name: str, radar_list: list):

        str_dict = {}
        delay = ''

        if len(radar_list) == 1: 
            activity = radar_list[0]
            key = activity['id']
            opening_string = f"Warning: radar detected on {road_name}: {activity['segment_start']} to {activity['segment_end']}."
            info_string = f"Radar located at HM {activity['location_hm']}."

            str_dict['type'] = 'radar'
            str_dict['key'] = key 
            str_dict['opening'] = opening_string
            str_dict['info'] = info_string
            str_dict['end'] = ''

        elif len(radar_list) > 1:
            opening_string = f"Warning: multiple radars detected on {road_name}: {activity['segment_start']} to {activity['segment_end']}."
            radars_list = []
            surr_key = []
            
            for activity in radar_list:
                key = activity['id']
                surr_key.append(key)
                
                info_string = f"Radar at HM {activity['location_hm']}."
                radars_list.append(info_string)
                
            surrogate_key = "-".join(surr_key)
            total_info = "\n".join(radars_list)

            str_dict['type'] = 'radar'
            str_dict['key'] = surrogate_key 
            str_dict['opening'] = opening_string
            str_dict['info'] = total_info
            str_dict['end'] = ''

        return str_dict, delay
        
    
    def create_msg(self, road_name: str, activity_list: list, segment_start: str, segment_end: str) -> str:

        radar_list = self.gather_activities(road_name, activity_list, segment_start, segment_end)

        radar_str_dict, radar_delay = self.construct_radar(road_name, radar_list)
        
        if len(radar_str_dict) > 0:
            radar_msg = f"{radar_str_dict['opening']}\n\n{radar_str_dict['info']}\n\n{radar_str_dict['end']}"
        else:
            radar_msg = ''
            
        return radar_msg, radar_delay