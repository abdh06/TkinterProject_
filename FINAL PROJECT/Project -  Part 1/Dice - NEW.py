from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import os  # Import os for handling file paths

# Function to get the relative path to an image
def resource_path(relative_path):
    base_path = os.path.dirname(__file__)  # Get the directory of the current script
    return os.path.join(base_path, relative_path)

root = Tk()
root.geometry("400x550")
root.title("Time to ROLL the Dice! - Project 1")
root.iconbitmap(resource_path('Dices/Dice - Title.ico'))  # Set the window icon

def Roll():
    Rolled = random.choice(Dicez)
    Rolling_label.config(image=Rolled)

    # Assign a new value to x each time Roll() is called
    global x
    if Rolled == One:
        x = "Yikes.. You rolled a one. \n Better luck next time!"
    elif Rolled == Two:
        x = "You Rolled a two. \n Well Atleast it's not a one, right?."
    elif Rolled == Three:
        x = "You rolled a three. \n Not too bad, not too good."
    elif Rolled == Four:
        x = "You rolled a four. \n Good one!"
    elif Rolled == Five:
        x = "You rolled a five! \n Now we're talking!"
    elif Rolled == Six:
        x = "You rolled a six! \n That's the best one there is!"

    Rolled2.config(text=x)

Rolling = Image.open(resource_path("Dices/rollingdice.gif"))
Rolling = ImageTk.PhotoImage(Rolling)

Rolling_label = Label(root, image=Rolling)
Rolling_label.grid(row=0, column=0, padx=50, pady=50)

One = ImageTk.PhotoImage(Image.open(resource_path("Dices/One.jpg")))
Two = ImageTk.PhotoImage(Image.open(resource_path("Dices/Two.jpg")))
Three = ImageTk.PhotoImage(Image.open(resource_path("Dices/Three.jpg")))
Four = ImageTk.PhotoImage(Image.open(resource_path("Dices/Four.jpg")))
Five = ImageTk.PhotoImage(Image.open(resource_path("Dices/Five.jpg")))
Six = ImageTk.PhotoImage(Image.open(resource_path("Dices/Six.jpg")))

Dicez = [One, Two, Three, Four, Five, Six]

Opening = Label(root, text="Are you ready to roll the dice!")
Opening.grid(row=1)

# Create Rolled2 label here
Rolled2 = Label(root, text="")
Rolled2.grid(row=4, pady=10)

Get_DiceN = Button(root, text="Roll The Dice!", command=Roll)
Get_DiceN.grid(row=2, pady=10)

root.mainloop()
