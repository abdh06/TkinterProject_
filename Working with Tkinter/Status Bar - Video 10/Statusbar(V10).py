from tkinter import *
from PIL import ImageTk, Image

def root_destroy():
    root.destroy()

def forward(image_number):
    global my_Label
    global button_back
    global button_forward
    global status
    
    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number])
    
    button_forward.config(command=lambda: forward(image_number + 1))
    button_back.config(command=lambda: back(image_number - 1))
    
    if image_number == len(image_list) - 1:
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL)
        
    button_back.config(state=NORMAL)  # Enable the back button since we're moving forward
   
    my_Label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2, padx=5, pady=5)
    button_back.grid(row=1, column=0, padx=5, pady=5)

    status.config(text="Image " + str(image_number + 1) + " out of " + str(len(image_list)))

def back(image_number):
    global my_Label
    global button_back
    global button_forward
    global status
    
    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number])
    
    button_forward.config(command=lambda: forward(image_number + 1))
    button_back.config(command=lambda: back(image_number - 1))
    
    if image_number == 0:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL)
        
    button_forward.config(state=NORMAL)  # Enable the forward button since we're moving backward
   
    my_Label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2, padx=5, pady=5)
    button_back.grid(row=1, column=0, padx=5, pady=5)

    status.config(text="Image " + str(image_number + 1) + " out of " + str(len(image_list)))

root = Tk()
root.title("Status Bar")
root.iconbitmap('c:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Icon, Images & Exit Buttons - Video 8/Cogwheel.ico')

image1 = ImageTk.PhotoImage(Image.open('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cubes.jpg'))
image2 = ImageTk.PhotoImage(Image.open('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Cat.jpg'))
image3 = ImageTk.PhotoImage(Image.open('C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Image Viewer App - Video 9/Elephant.jpg'))

image_list = [image1, image2, image3]

my_Label = Label(image=image1)
my_Label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=lambda: back(0), state=DISABLED, width=10)
Button_quit = Button(root, text="Quit Program", command=root_destroy, padx=10, width=15)
button_forward = Button(root, text=">>", command=lambda: forward(1), width=10)

button_back.grid(row=1, column=0, padx=5, pady=5)
Button_quit.grid(row=1, column=1, padx=5, pady=5)
button_forward.grid(row=1, column=2, padx=5, pady=5)

status = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
