class api_parser:

    def __init__(self, repsonse):

        self.response = repsonse

    
    def parse_response(self):

        response_dt = self.response["dateTime"]
        roads = self.response["roads"]

        rw_list = [] 
        ja_list = []
        rd_list = []

        for road in roads:
            road_name = road["road"]
            segments = road["segments"]

            for segment in segments:
                try:
                    segment_start = segment["start"]
                    segment_end = segment["end"]
                except:
                    segment_start = "" 
                    segment_end = ""

                if 'roadworks' in dict(segment).keys():
                    roadworks = segment["roadworks"]

                    for roadwork in roadworks:
                        rw_dict = {}
                        rw_dict['id'] = roadwork["id"]
                        rw_dict['datetime'] = response_dt
                        rw_dict['road_name'] = road_name
                        rw_dict['segment_start'] = segment_start
                        rw_dict['segment_end'] = segment_end
                        rw_dict['event_name'] = roadwork["category"]
                        rw_dict['roadworks_start'] = roadwork["from"]
                        rw_dict['roadworks_end'] = roadwork["to"]
                        rw_dict['incident'] = roadwork["incidentType"]
                        rw_dict['description'] = roadwork["reason"]
                        rw_dict['start_time'] = roadwork["start"]
                        rw_dict['end_time'] = roadwork["stop"]

                        rw_list.append(rw_dict)

                if 'jams' in dict(segment).keys():
                    jams = segment["jams"]

                    for jam in jams:
                        ja_dict = {}
                        ja_dict['id'] = jam["id"]
                        ja_dict['datetime'] = response_dt
                        ja_dict['road_name'] = road_name
                        ja_dict['segment_start'] = segment_start
                        ja_dict['segment_end'] = segment_end
                        ja_dict['event_name'] = jam["category"]
                        ja_dict['jam_start'] = jam["from"]
                        ja_dict['jam_end'] = jam["to"]
                        try:
                            ja_dict['jam_starttime'] = jam["start"]
                        except:
                            ja_dict['jam_starttime'] = "<unknown or not applicable>"
                        try: 
                            ja_dict['delay'] = jam["delay"]
                        except:
                            ja_dict['delay'] = ''
                        ja_dict['incident'] = jam["incidentType"]
                        ja_dict['description'] = jam["reason"]

                        ja_list.append(ja_dict)

                if 'radars' in dict(segment).keys():
                    radars = segment['radars']

                    for radar in radars:
                        ra_dict = {}
                        ra_dict['id'] = radar["id"]
                        ra_dict['datetime'] = response_dt
                        ra_dict['road_name'] = road_name
                        ra_dict['segment_start'] = segment_start
                        ra_dict['segment_end'] = segment_end
                        ra_dict['event_name'] = radar["category"]
                        ra_dict['radar_between_1'] = radar["from"]
                        ra_dict['radar_between_2'] = radar["to"]
                        ra_dict['what'] = radar["events"][0]["text"]
                        ra_dict['location_hm'] = radar["HM"]
                        ra_dict['location'] = radar["reason"]

                        rd_list.append(ra_dict)


        return rw_list, ja_list, rd_list