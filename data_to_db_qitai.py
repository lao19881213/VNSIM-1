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
data_qitai_square = np.loadtxt('./DATABASE/qitai_square.txt', dtype=float)
#print(data_qitai_square)
data_qitai_square[:,0] = data_qitai_square[:,0]/1000.0
data_qitai_square[:,1] = data_qitai_square[:,1]/1000.0
data_qitai_square[:,2] = data_qitai_square[:,2]/1000.0
#print(data_qitai_square)
for mm in range(data_qitai_square.shape[0]):
       qitai_square_name = 'qitai_square_new_%s' % str(mm+1)
       qitai_square_x = data_qitai_square[mm,0]
       qitai_square_y = data_qitai_square[mm,1]
       qitai_square_z = data_qitai_square[mm,2]
       qitai_square_el = '10.0'
       qitai_square_type = '0'
       sql = 'INSERT INTO table_vlbi (vlbi_name, vlbi_x, vlbi_y, vlbi_z, vlbi_el, vlbi_type) VALUES("' \
         + qitai_square_name + '",' + str(qitai_square_x) + "," + str(qitai_square_y) + ',' + str(qitai_square_z) + ',' + qitai_square_el + ',' + qitai_square_type + ')'

       with sqlite3.connect(myDb.db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

myDb.write_to_pickle()

