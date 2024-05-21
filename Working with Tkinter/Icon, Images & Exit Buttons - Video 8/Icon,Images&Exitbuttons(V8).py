from tkinter import *
from PIL import ImageTk, Image

def root_destroy():
    root.destroy()

root = Tk()
root.title("Icons, Images, and Exit Buttons")
root.iconbitmap('c:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Icon, Images & Exit Buttons - Video 8/Cogwheel.ico')
root.geometry("400x400")

# Open the first image file
image1 = Image.open('c:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Icon, Images & Exit Buttons - Video 8/Transparency Dices.png')

# Resize the first image if necessary
image1 = image1.resize((300, 300))

# Convert the first image to a PhotoImage object
image1_photo = ImageTk.PhotoImage(image1)
MyLabel = Label(image=image1_photo) 
MyLabel.pack()

# Open the second image file
image2 = Image.open('c:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/Icon, Images & Exit Buttons - Video 8/Green Emerald.png')

# Resize the second image
resized_image = image2.resize((20, 20))  # Adjust the size as needed

# Convert the resized image to a PhotoImage object
myimginbutton = ImageTk.PhotoImage(resized_image)

# Create the button with the second image and text
Button_quit = Button(root, image=myimginbutton, text="Quit", command=root_destroy, compound="left", padx=10)
Button_quit.pack(pady=20)

root.mainloop()
