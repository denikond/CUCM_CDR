import csv
import pandas
import sqlite3
from os import listdir
from os.path import isfile, join

cdr_table_name = 'cdr_table'
cmr_table_name = 'cmr_table'
CDR = 'CDR'

def main():
    con = sqlite3.connect("my.db") # change to 'sqlite:///your_filename.db'
    #con = sqlite3.connect(":memory:")  # change to 'sqlite:///your_filename.db'
    cur = con.cursor()

    num_count: int = 1
    for fi in listdir(CDR):
        csv_file = join(CDR,fi)
        if isfile(csv_file):
            with open(csv_file, 'r') as csvfile:
                print(num_count,'Importing data from', fi)
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




'''
    cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

    with open('data.csv','r') as fin: # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['col1'], i['col2']) for i in dr]

    cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
    con.commit()
    con.close()
'''





if __name__ == "__main__":
    main()
