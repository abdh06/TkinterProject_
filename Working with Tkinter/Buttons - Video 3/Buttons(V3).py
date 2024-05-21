from tkinter import *

root = Tk()
root.geometry("400x300")  # Set the window size to 400x300 pixels

def Disable():
    myButton.config(state=DISABLED, fg="Red", text= "unclickable")
    Button2.config(state=NORMAL, fg = "green")

def Enable():
    myButton.config(state=NORMAL, fg = "black", text = "Click this button for a surprise!")
    Button2.config(state=DISABLED, fg = "black")

myButton = Button(root, text="Click This Button for a surprise!", command=Disable, padx=20, pady=10)
myButton.grid(row=0, column=0)

Button2 = Button(root, text="Re-enable button", command=Enable, state=DISABLED, padx=20, pady=10)
Button2.grid(row=1, column=1)

root.mainloop()