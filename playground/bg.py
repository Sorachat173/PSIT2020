from tkinter import *

class Wallpaper():
    def background(self, master):
        canvas = Canvas(master)
        self.photo = PhotoImage(file = 'image/bg.png')
        canvas.create_image(500, 280, image=self.photo)
        canvas.grid()

root = Tk()
test = Wallpaper()
test.background(root)
root.minsize(1000, 563)
root.maxsize(1000, 563)
root.mainloop()

