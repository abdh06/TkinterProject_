from tkinter import *  # Import tkinter for GUI
from tkinter import messagebox  # Import messagebox from tkinter for displaying messages
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL for handling images
import time  # Import time for measuring reaction time
import random  # Import random for selecting buttons randomly

# Window with the game
def open_game_window():
    game_window = Toplevel()  # Create a new top-level window for the game
    game_window.title("Reaction Game")  # Set the title of the game window
    game_window.geometry("450x100")  # Set the size of the game window
    game_window.iconbitmap("C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/FINAL PROJECT/Project - Part 2/Happy.ico")  # Set the window icon

    def start_game():
        game_window.iconbitmap("C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/FINAL PROJECT/Project - Part 2/Happy.ico")  # Set the window icon to happy face
        start_button.config(state=DISABLED, text="Start!")  # Disable the start button and change its text
        left_button.config(state=NORMAL, bg="SystemButtonFace")  # Enable the left button and reset its color
        right_button.config(state=NORMAL, bg="SystemButtonFace")  # Enable the right button and reset its color
        global random_button  # Declare random_button as global to use it across functions
        random_button = random.choice([left_button, right_button])  # Randomly select either the left or right button
        random_button.config(bg="orange")  # Highlight the selected button in orange
        global start_time  # Declare start_time as global to use it across functions
        start_time = time.time()  # Record the current time as the start time

    def left_clicked():
        check(left_button)  # Call check function with the left button when it is clicked

    def right_clicked():
        check(right_button)  # Call check function with the right button when it is clicked

    def check(Button_Clicked):
        global random_button  # Use the global random_button variable
        global Wrong_Button  # Use the global Wrong_Button variable
        if Button_Clicked == random_button:  # If the clicked button is the highlighted button
            random_button.config(bg="light green")  # Change the button color to green
            calculate_reaction_time()  # Calculate and display the reaction time
        else:
            Wrong_Button = Button_Clicked  # Set the clicked button as the wrong button
            reset_game()  # Reset the game state

    def reset_game():
        game_window.iconbitmap("C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/FINAL PROJECT/Project - Part 2/sad.ico")  # Change the window icon to sad face
        result_label.config(text="Wrong button clicked! Try again.")  # Update the result label with an error message
        Wrong_Button.config(bg="red")  # Change the wrong button color to red
        random_button.config(bg="SystemButtonFace")  # Reset the highlighted button color
        left_button.config(state=DISABLED)  # Disable the left button
        right_button.config(state=DISABLED)  # Disable the right button
        start_button.config(state=NORMAL, text="Restart?")  # Enable the start button and change its text to "Restart?"

    def calculate_reaction_time():
        left_button.config(state=DISABLED)  # Disable the left button
        right_button.config(state=DISABLED)  # Disable the right button
        reaction_time = time.time() - start_time  # Calculate the reaction time
        result_label.config(text=f"Nice! Your reaction time: {reaction_time:.3f} seconds")  # Display the reaction time
        start_button.config(state=NORMAL, text="Restart?")  # Enable the start button and change its text to "Restart?"

    # Create left and right buttons, initially disabled
    left_button = Button(game_window, text="Left", width=10, command=left_clicked, state=DISABLED)
    left_button.pack(side=LEFT, padx=10)  # Pack the left button to the left side with padding
    right_button = Button(game_window, text="Right", width=10, command=right_clicked, state=DISABLED)
    right_button.pack(side=RIGHT, padx=10)  # Pack the right button to the right side with padding

    # Create the start button
    start_button = Button(game_window, text="Start!", width=10, command=start_game)
    start_button.pack()  # Pack the start button

    # Create the result label
    result_label = Label(game_window, text="")
    result_label.pack(pady=10)  # Pack the result label with padding

# Function to display instructions
def message():
    messagebox.showinfo("How to play", """Click the 'Start' button to begin the game. 
Once the game starts, a button will light up. 
Click on the button as quickly as you can. 
Your reaction time will be displayed after each click.""")  # Show the instructions in a message box

# Main window
root = Tk()  # Create the main window
root.geometry("400x200")  # Set the size of the main window
root.title("Reaction Game")  # Set the title of the main window
root.iconbitmap("C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/FINAL PROJECT/Project - Part 2/Happy.ico")  # Set the window icon

# Load the background image
bg_image = Image.open("C:/Users/abdher/OneDrive - Arenaskolor/Skrivbordet/School/PGR/Prog1/Working with Tkinter/FINAL PROJECT/Project - Part 2/Emojis.jpg")  # Open the image
bg_image = bg_image.resize((400, 200))  # Resize the image
bg_photo = ImageTk.PhotoImage(bg_image)  # Convert the image to PhotoImage

# Set the background image
background_label = Label(root, image=bg_photo)  # Create a label with the background image
background_label.image = bg_photo  # Keep a reference to the image
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the label to cover the entire window

# Create a frame for buttons and title with a black border
frame = LabelFrame(root, highlightbackground="black", highlightthickness=1)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the frame in the window

# Title label
title_label = Label(frame, text="Welcome to the Reaction Game!", font=("Helvetica", 16))
title_label.pack(pady=10)  # Pack the title label with padding

# Create start button
start_button = Button(frame, text="Play the game!", width=10, command=open_game_window)
start_button.pack(pady=10)  # Pack the start button with padding

# Create instructions button
instructions_button = Button(frame, text="How to Play", width=10, command=message)
instructions_button.pack(pady=10)  # Pack the instructions button with padding

root.mainloop()  # Start the applicatoin on main loop to exit only when needed.
