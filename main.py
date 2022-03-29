#import csv
import os
#import sqlite3
import pandas
from os import listdir
from os.path import isfile, join
import sqlalchemy
import config
import time

cdr_table_name = 'cdr_table'
cmr_table_name = 'cmr_table'
CDR = 'CDR'


def main():
    s_engine = 'mssql+pyodbc://' + config.Username + ':' \
        + config.UPass + '@' + config.ServerName + '/' + config.Database \
        + '?trusted_connection=no' + config.Driver
    engine = sqlalchemy.create_engine(s_engine)
    con = engine.connect()
    # con = sqlite3.connect("my.db") # change to 'sqlite:///your_filename.db'
    # con = sqlite3.connect(":memory:")  # change to 'sqlite:///your_filename.db'
    #cur = con.cursor()

    while True:
        num_count: int = 1
        for fi in listdir(CDR):
            csv_file = join(CDR, fi)
            if isfile(csv_file):
                with open(csv_file, 'r') as csvfile:
                    print(num_count, 'Importing data from', fi)
                    num_count += 1
                    df = pandas.read_csv(csvfile)
                    df.drop(0, axis=0, inplace=True)
                    print(df)
                    if fi[0:3] == 'cdr':
                        table_name = cdr_table_name
                    else:
                        table_name = cmr_table_name
                    try:
                        df.to_sql(table_name, con, if_exists='append', index=False)
                    except Exception as err:
                        print(err)
                    else:
                        os.remove(csv_file)
                    #aa = session.query(cmr_table_name).first()
        time.sleep(60)


if __name__ == "__main__":
    main()
