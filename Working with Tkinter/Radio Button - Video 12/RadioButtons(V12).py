from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Radio Buttons")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')



def update(value):
    MyLabel = Label(root, text=value)
    MyLabel.pack()

MODES = [
    ("Math", 1),
    ("Programming", 2),
    ("English", 3)
]

Subject = IntVar()
Subject.set(1)

for text, mode in MODES:
    Radiobutton(root, text=text, variable=Subject, value=mode).pack(anchor=W)

# This is a Variable with a value that can be changed.
#r = IntVar()

# If r is set to one of the 3 values, that option is automatically chosen. (Good for "saving" ones process.)
# Example:  r.set("3") --> Option 3 is automatically chosen.

# 3 Options with the r.
# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: update(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: update(r.get())).pack()
# Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: update(r.get())).pack()

# Button that shows current value
b = Button(root, text="click for value!", command=lambda: update(Subject.get()))
b.pack()

mainloop()