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
data_array = np.loadtxt('./DATABASE/%s' % args.array_data, dtype=float)
#print(data_array)
data_array[:,0] = data_array[:,0]
data_array[:,1] = data_array[:,1]
data_array[:,2] = data_array[:,2]
#print(data_array)
for mm in range(data_array.shape[0]):
       array_name = '%s_%s' % (args.array_data, str(mm+1))
       array_x = data_array[mm,0]
       array_y = data_array[mm,1]
       array_z = data_array[mm,2]
       array_el = '10.0'
       array_type = '0'
       sql = 'INSERT INTO table_vlbi (vlbi_name, vlbi_x, vlbi_y, vlbi_z, vlbi_el, vlbi_type) VALUES("' \
         + array_name + '",' + str(array_x) + "," + str(array_y) + ',' + str(array_z) + ',' + array_el + ',' + array_type + ')'

       with sqlite3.connect(myDb.db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

myDb.write_to_pickle()

