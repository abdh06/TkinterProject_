from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Checkboxes")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')
root.geometry("400x400")

# Dropdown Boxes

var = StringVar()
var  .set("Math")

def ShowChoice():
    MY_Label = Label(root, text=var.get())
    MY_Label.pack()

# Create Dropdown menu

Options =  [
    "Math", 
    "English", 
    "Swedish", 
    "Programming", 
    "Help"    
]
 
drop = OptionMenu(root, var, *Options)
drop.pack()

button = Button(root, text="print the choice!", command=ShowChoice)
button.pack()

root.mainloop()