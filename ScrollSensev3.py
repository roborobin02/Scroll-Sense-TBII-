import tkinter as tk
from src.helpers import set_background, clear_widgets

# create the gui frame
root = tk.Tk()
root.title("ScrollSense")
# size the size of the frame
screen_width = 350
screen_height = 750

root.minsize(screen_width, screen_height)


def create_new_page(root):
    """This function creates a new page that will clear all the widgets
    that were previously generated, changes the background colour and places a button that will go back"""

    # clears the widgets - the image and the button
    clear_widgets(root)

    # change the background colour of the frame
    root.configure(background="pink")

    # place a button that will go back
    back_button = tk.Button(root,
                            text="GO BACK",
                            font=("Comic Sans MS", 14, "bold"),
                            command=lambda: create_startpage(root, image_file_path) #="/Users/robinpaul/Desktop/TechBasics2/images/homepage.jpg")
                            )

    back_button.place(relx=0.5,
                      rely=0.925)

    # We covered this in TBI - a button that closes the game
    exit_button = tk.Button(text="X",
                            font=("Comic Sans MS", 14, "bold"),
                            command=root.destroy
                            )
    exit_button.pack(side="bottom", anchor='e')
    exit_button.place(relx=0.6,
                      rely=0.925)

def create_startpage(root, image_file_path):
    """This definition creates the homepage.
    It places a background image and places a button at the bottom"""

    # place a background image on the home page using the set background definition
    set_background(root, image_file_path) #="/Users/robinpaul/Desktop/TechBasics2/images/homepage.jpg")

    # place a button that will go a new page
    newpage_button = tk.Button(root,
                               text="CLICK HERE TO GO TO THE NEXT PAGE",
                               font=("Ubuntu", 14, "bold"),
                               command=lambda: create_new_page(root)
                               )
    newpage_button.pack(side="bottom")


image_file_path = 'images/homepage.jpg'
create_startpage(root, image_file_path)

root.mainloop()