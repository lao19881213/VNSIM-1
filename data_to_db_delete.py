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
data_moon = np.loadtxt('xyz_EME2000_230601_230701',usecols =(6,7,8))
#print(data_moon)
data_moon[:,0] = data_moon[:,0]/1000
data_moon[:,1] = data_moon[:,1]/1000
data_moon[:,2] = data_moon[:,2]/1000

for mm in range(data_moon.shape[0]):
    if (mm>=3639):
       moon_name = 'moon_%s' % mm
       moon_x = data_moon[mm,0]
       moon_y = data_moon[mm,1]
       moon_z = data_moon[mm,2]
       moon_el = '10.0'
       moon_type = '0'
       #sql = 'INSERT INTO table_vlbi (vlbi_name, vlbi_x, vlbi_y, vlbi_z, vlbi_el, vlbi_type) VALUES("' \
       #  + moon_name + '",' + str(moon_x) + "," + str(moon_y) + ',' + str(moon_z) + ',' + moon_el + ',' + moon_type + ')'
       
       sql = 'DELETE FROM table_vlbi WHERE vlbi_name="' + moon_name + '"'

       with sqlite3.connect(myDb.db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

myDb.write_to_pickle()

