from Func_db import DbModel
import tkinter as tk
import sqlite3
import argparse

db_file = 'database.db'
pkl_file = 'database.pkl'

    # test DbEditor
#my_window = tk.Tk()
    # my_window.resizable(False, False)
#my_window.title("Database Editor")
#mydb_e=DbEditor(my_window, db_file, pkl_file)
#my_window.mainloop()
myDb=DbModel(db_file, pkl_file)

myDb.write_to_pickle()
def parse_args():
        parser = argparse.ArgumentParser(description="insert source pos")
        parser.add_argument('-r',
                            '--src_ra',
                            default='00h00m00s',
                            help='Specify the source ra pos')
        parser.add_argument('-d',
                            '--src_dec',
                            default='30d00m00s',
                            help='Specify the source dec pos')
        parser.add_argument('-n',
                            '--src_name',
                            default='RA00DEC30',
                            help='Specify the source name')

        return parser.parse_args()


args = parse_args()

sql = 'INSERT INTO table_src (src_name, src_ra, src_dec) VALUES("' \
                              + args.src_name + '","' + args.src_ra + '","' + args.src_dec + '")'

with sqlite3.connect(myDb.db_path) as conn:
     cur = conn.cursor()
     cur.execute(sql)
     conn.commit()

myDb.write_to_pickle()

