from tkinter import *

window = Tk()
Label(window, text="Your Job: ").grid(row=0, column=0)
Entry(window).grid(row=0, column=1)

window.mainloop()