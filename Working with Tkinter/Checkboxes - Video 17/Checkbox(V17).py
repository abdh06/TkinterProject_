from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Checkboxes")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')
root.geometry("400x400")

var = IntVar()

def Showbox():
    Show = Label(root, text=var.get()).pack()

c1 = Checkbutton(root, text="Checkbox 1", variable=var)
c1.pack()

Show = Label(root, text=var.get()).pack()

ShowButton = Button(root, text="Show the box value!", command=Showbox)
ShowButton.pack()

mainloop()