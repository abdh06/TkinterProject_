from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Adding Frames")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')

frame = LabelFrame(root, text="This is my Frame...", padx=10,pady=10)
frame.pack(padx=10,pady=10)

b = Button(frame, text="This is a test!")
b2 = Button(frame, text="This is also a test!")
b.grid(row=1, column=0)
b2.grid(row=2, column=0)
root.mainloop()