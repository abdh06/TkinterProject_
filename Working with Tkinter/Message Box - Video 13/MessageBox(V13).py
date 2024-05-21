from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')

def oshadi():
        messagebox.showinfo("Hello!", "This is obviously (not) a test. \n We are informing you, that you've been hacked.")

Button(root, text="Popup", command=lambda: oshadi()).pack()

mainloop()