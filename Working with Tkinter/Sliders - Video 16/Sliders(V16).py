from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Open File")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')
# This is a Vertical Slider.
vertical = Scale(root, from_=0, to=900)
vertical.pack()

# This is a Horizontal Slider.
horizontal = Scale(root, from_=0, to=900, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()

def slide():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
b = Button(root, text="Click me!", command=lambda: slide()).pack()

mainloop()