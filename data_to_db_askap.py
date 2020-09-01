from Func_db import DbModel
import tkinter as tk
import sqlite3
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

import numpy as np
data_askap = np.loadtxt('./DATABASE/askap_array', dtype=float)
#print(data_askap)
data_askap[:,0] = data_askap[:,0]#/1000.0
data_askap[:,1] = data_askap[:,1]#/1000.0
data_askap[:,2] = data_askap[:,2]#/1000.0
#print(data_askap)
for mm in range(data_askap.shape[0]):
       askap_name = 'askap_new1_%s' % str(mm+1)
       askap_x = data_askap[mm,0]
       askap_y = data_askap[mm,1]
       askap_z = data_askap[mm,2]
       askap_el = '10.0'
       askap_type = '0'
       sql = 'INSERT INTO table_vlbi (vlbi_name, vlbi_x, vlbi_y, vlbi_z, vlbi_el, vlbi_type) VALUES("' \
         + askap_name + '",' + str(askap_x) + "," + str(askap_y) + ',' + str(askap_z) + ',' + askap_el + ',' + askap_type + ')'

       with sqlite3.connect(myDb.db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

myDb.write_to_pickle()

