# import pandas as pd

# x = pd.read_csv("db_inminder.csv", delimiter=",")
# print(x)

from tkinter import *
import csv
import datetime

def enter_button():
    now = datetime.datetime.now()
    amount = e1.get()# That is where I thought I should get the Input from the widget
    with open('File.csv', 'a') as f:
        w = csv.writer(f,dialect='excel-tab')
        w.writerow([now.strftime("%Y-%m-%d %H:%M"), amount]) # write Date/Time and the value
    f.close()

master = Tk()
e1 = Entry(master)
Label(master, text='Enter Number Here').grid(row=0)
myButton=Button(master,text='Enter',command=enter_button)
e1.grid(row=0,column=1)
myButton.grid(row=1,column=0)
mainloop()