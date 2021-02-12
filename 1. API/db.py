import sqlite3
import os
import pandas as pd


class DB:

    def __init__(self):
        pass

    def print_cwd(self):
        self.path = os.getcwd()
        print(os.getcwd())

    def connect(self, path):
        conn = sqlite3.connect(path)
        return conn
    
    def select_top(self, conn):
        query = "SELECT * FROM lending_data;"
        df = pd.read_sql_query(query, con=conn)
        df = df.head()
        return df.to_dict()
