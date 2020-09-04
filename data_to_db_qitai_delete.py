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
    parser = argparse.ArgumentParser(description="insert array data")
    parser.add_argument('-a',
                        '--array_data',
                        default='qitai_square',
                        help='Specify the obser array data')


    return parser.parse_args()
                          

args = parse_args()
import numpy as np
#data_array = np.loadtxt('./DATABASE/%s' % args.array_data, dtype=float)
#print(data_array)
#data_array[:,0] = data_array[:,0]
#data_array[:,1] = data_array[:,1]
#data_array[:,2] = data_array[:,2]
for mm in range(16):
       array_name = '%s_%s' % (args.array_data, str(mm+1))
       sql = 'DELETE FROM table_vlbi WHERE vlbi_name="' + array_name + '"'

       with sqlite3.connect(myDb.db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

myDb.write_to_pickle()

