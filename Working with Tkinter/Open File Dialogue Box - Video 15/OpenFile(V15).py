from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Open File")
root.iconbitmap('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cogwheel.ico')

def filename():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter", title="Select a file:", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
    
    global my_label
    global my_image
    global my_image_label

    # Show us the File Destination
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


Open_File = Button(root, text="Click to show your pictures!", command=lambda: filename())
Open_File.pack()


root.mainloop()