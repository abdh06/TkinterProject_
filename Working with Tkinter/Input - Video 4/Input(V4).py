from tkinter import *
 
root = Tk()
e = Entry(root, width=50, bg="Black", fg ="white")
e.pack()
e.insert(0, "Enter your text here:")
# Creating a Label Widget
mylabel = Label(root, text = "Hello World!")

# Shoving it onto the screen
mylabel.pack()

root.mainloop() 