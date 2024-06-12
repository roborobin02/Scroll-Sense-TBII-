import tkinter as tk
from src.helpers import set_background, clear_widgets

# create the gui frame
root = tk.Tk()
root.title("ScrollSense")
# size the size of the frame
screen_width = 350
screen_height = 750

# so that you cant resize the scren
root.minsize(screen_width, screen_height)
root.maxsize(screen_width, screen_height)


# main script content
def create_new_page(root):
    """This function creates a new page that will clear all the widgets,
    change the background colour, and place a button to go back."""
    clear_widgets(root)
    root.configure(background="pink")

    back_button = tk.Button(root, text="GO BACK", font=("Comic Sans MS", 14, "bold"),
                            command=lambda: create_startpage(root, image_file_path))
    back_button.place(relx=0.5, rely=0.925, anchor="center")

    exit_button = tk.Button(root, text="X", font=("Comic Sans MS", 14, "bold"),
                            command=root.destroy)
    exit_button.place(relx=0.6, rely=0.925, anchor="center")


def create_startpage(root, image_file_path):
    """This function creates the homepage with a background image and places a button at the bottom."""
    set_background(root, image_file_path)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)

    intro_label = tk.Label(intro_frame, text="Welcome to the ScrollSense Prototype!\nPlease enter your name:",
                           bg="white", font=("Comic Sans MS", 14))
    intro_label.place(relx=0.5, rely=0.6, anchor="center")

    name_entry = tk.Entry(intro_frame, font=("Comic Sans MS", 12))
    name_entry.place(relx=0.5, rely=0.65, anchor="center")

    daily_time_label = tk.Label(intro_frame, text="Please tell me your daily time on Instagram (in Hours):",
                                bg="white", font=("Comic Sans MS", 14))
    daily_time_label.place(relx=0.5, rely=0.7, anchor="center")

    daily_time_entry = tk.Entry(intro_frame, font=("Comic Sans MS", 12))
    daily_time_entry.place(relx=0.5, rely=0.75, anchor="center")

    newpage_button = tk.Button(root, text="CLICK HERE TO GO TO THE NEXT PAGE", font=("Ubuntu", 14, "bold"),
                               command=lambda: create_new_page(root))
    newpage_button.place(relx=0.5, rely=0.925, anchor="center")


image_file_path = 'images/ScrollSenseScreenshot1.jpg'
create_startpage(root, image_file_path)

root.mainloop()