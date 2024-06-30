from sqlalchemy import create_engine
import pandas as pd
import os

from dotenv import load_dotenv

class DAO:

    def __init__(self, rw_list: list, ja_list: list, rd_list: list):

        print("init")
        load_dotenv()
        db_user = os.getenv("db_username")
        db_pwd = os.getenv("db_password")
        db_ip = os.getenv("db_ip")
        self.engine = create_engine(f'mysql+pymysql://{db_user}:{db_pwd}@{db_ip}/traffic_db')
        self.rw_list = rw_list
        self.ja_list = ja_list
        self.rd_list = rd_list

    
    def insert(self, df: pd.DataFrame, name: str) -> None:
        
        df.to_sql(name, con=self.engine, if_exists='replace')

    
    def create_df(self, input_list: list) -> pd.DataFrame:

        df = pd.DataFrame.from_records(input_list)

        return df 
    

    def insert_data(self) -> str:

        rw_df = self.create_df(self.rw_list)
        ja_df = self.create_df(self.ja_list)
        rd_df = self.create_df(self.rd_list)

        self.insert(rw_df, "stg_anwb_roadworks")
        self.insert(ja_df, "stg_anwb_jams")
        self.insert(rd_df, "stg_anwb_radars")
        
        resp = "Tables succesfully inserted"

        return resp