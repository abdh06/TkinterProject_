from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Opening Another Window")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')

def open():
    
    Top = Toplevel()
    Top.title("Second Window")

    global label
    label = Label(Top, text="Jump.")
    label.pack()


Open = Button(root, text="Open the new window", command=lambda: open())
Open.pack()

mainloop()