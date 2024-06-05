
# Importing everything we need to run the app
import tkinter as tk
from PIL import Image, ImageTk
import random


# Function to clear all widgets within a frame and destroy the frame itself
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.destroy()


# Function to set the background image for a frame
# Using ImageTk to load the image and create a label with the image
def set_background(frame, image):
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(frame, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)


# Function to generate a random exercise from a predefined list
def generate_random_exercise():
    exercises = ["full-body workout", "yoga session", "cardio routine", "strength training"]
    return random.choice(exercises)

def calculate_duolingo_lessons(hours_spent):
    # Assuming it takes 30 minutes to complete a Duolingo lesson
    minutes_for_one_lesson = 30
    total_minutes = hours_spent * 60
    return int(total_minutes / minutes_for_one_lesson)

def calculate_walk_distance(hours_spent):
    # Calculating the distance one could have walked, assuming the average person walks 5 km per hour
    average_walking_speed = 5
    return hours_spent * average_walking_speed

def calculate_reading_pages(hours_spent):
    # Calculating the amount of pages assuming the average person reads 40 pages per hour
    pages_per_hour = 40
    return int(hours_spent * pages_per_hour)

def calculate_watch_percentage(hours_spent):
    # Calculating percentage of how much of the Lord of the Rings franchise you could have watched
    total_minutes = 600
    percentage_watched = (hours_spent * 60 / total_minutes) * 100
    return percentage_watched

# Choosing a random activity from above and calculating the value based on player input
# Outputting a text with the finished numbers
def generate_random_activity(label, username, time_spent_on_instagram):
    # Clear the label content before updating
    label["text"] = ""

    activity_choice = random.choice(["reading", "watching", "walking", "duolingo", "exercise"])

    if activity_choice == "reading":
        label["text"] = f"{username}, you have spent {time_spent_on_instagram:.2f} hours on Instagram today.\nIn this time, you could have read {calculate_reading_pages(time_spent_on_instagram)} pages of your favorite book!"
    elif activity_choice == "watching":
        label["text"] = f"{username}, you have spent {time_spent_on_instagram:.2f} hours on Instagram today.\nIn this time, you could have watched {calculate_watch_percentage(time_spent_on_instagram):.2f}% of the whole Lord of the Rings franchise!\n AND THAT TAKES FOREVER"
    elif activity_choice == "walking":
        label["text"] = f"{username}, you have spent {time_spent_on_instagram:.2f} hours on Instagram today.\nIn this time, you could have walked {calculate_walk_distance(time_spent_on_instagram):.2f} km and taken in the fresh air!"
    elif activity_choice == "duolingo":
        label["text"] = f"{username}, you have spent {time_spent_on_instagram:.2f} hours on Instagram today.\nIn this time, you could have completed {calculate_duolingo_lessons(time_spent_on_instagram)} Duolingo lessons\n and made progress toward learning a new language!"
    elif activity_choice == "exercise":
        label["text"] = f"{username}, you have spent {time_spent_on_instagram:.2f} hours on Instagram today.\nIn this time, you could have completed a {generate_random_exercise()} workout!"


# Function to initiate the introductory screen, on it you can see an introductory text
# an entry for your name and for your daily instagram usage
def show_intro_screen(root, images):
    intro_frame = tk.Frame(root)
    intro_frame.pack(side="top", fill="both", expand=True)
    set_background(intro_frame, images[0])

    intro_label = tk.Label(intro_frame, text="Welcome to the ScrollSense Prototype!\nPlease enter your name:")
    intro_label.place(x=270, y=450, anchor="center")

    name_entry = tk.Entry(intro_frame)
    name_entry.place(x=270, y=500, anchor="center")

    daily_time_label = tk.Label(intro_frame, text="Please tell me your daily time on Instagram (in Hours):")
    daily_time_label.place(x=270, y=550, anchor="center")

    daily_time_entry = tk.Entry(intro_frame)
    daily_time_entry.place(x=270, y=600, anchor="center")

    next_button = tk.Button(intro_frame, text="Next", command=lambda: show_instagram_warning(intro_frame, root, images, name_entry.get(), daily_time_entry.get()))
    next_button.place(x=270, y=650, anchor="center")

# This screen is only supposed to simulate the act of opening instagram when youre bored
def show_instagram_warning(prev_frame, root, images, username, daily_time):
    clear_frame(prev_frame)

    warning_frame = tk.Frame(root)
    warning_frame.pack(side="top", fill="both", expand=True)
    set_background(warning_frame, images[1])

    warning_label = tk.Label(warning_frame, text="You are about to open Instagram.\n"
                                                 "But before Instagram will be opened, the ScrollSense app will intervene!")
    warning_label.place(x=270, y=300, anchor="center")

    instagram_button = tk.Button(warning_frame, text="Open Instagram", command=lambda: show_usage_screen(warning_frame, root, images, username, daily_time))
    instagram_button.place(x=270, y=350, anchor="center")

    exit_button = tk.Button(warning_frame, text="I want to spend my time otherwise", command=root.destroy)
    exit_button.place(x=270, y=400, anchor="center")

# This screen is what my app will be in the future, in the future it will have a breating exercise, displayed
# by an animation. During this animation you will be presented with your statistics, just like here.
# Here you have a text, which gives you stats based on what you have entered in the first screen.
def show_usage_screen(prev_frame, root, images, username, daily_time):
    clear_frame(prev_frame)

    usage_frame = tk.Frame(root)
    usage_frame.pack(side="top", fill="both", expand=True)
    set_background(usage_frame, images[2])

    time_spent_on_instagram = float(daily_time)
    reading_pages = calculate_reading_pages(time_spent_on_instagram)

    usage_label = tk.Label(usage_frame, text=f"{username}, you have spent "
                                             f"{time_spent_on_instagram} hours on Instagram today.\nIn this time,"
                                             f" you could have read {reading_pages} pages of your favorite book!")
    usage_label.place(x=270, y=150, anchor="center")

    generate_button = tk.Button(usage_frame, text="Generate Another Option", command=lambda: generate_random_activity(usage_label, username, time_spent_on_instagram))
    generate_button.place(x=270, y=200, anchor="center")

    next_button = tk.Button(usage_frame, text="Next", command=lambda: show_instagram_screen(usage_frame, root, images))
    next_button.place(x=270, y=250, anchor="center")

# This screen shows you that you will still end up on instagram and the app itself does not stop you form using it
def show_instagram_screen(prev_frame, root, images):
    clear_frame(prev_frame)

    instagram_frame = tk.Frame(root)
    instagram_frame.pack(side="top", fill="both", expand=True)
    set_background(instagram_frame, images[3])

    instagram_label = tk.Label(instagram_frame, text="Welcome to Instagram!")
    instagram_label.place(x=270, y=20, anchor="center")

    next_button = tk.Button(instagram_frame, text="Next", command=lambda: show_concept_screen(instagram_frame, root, images))
    next_button.place(x=270, y=50, anchor="center")

# This screen provides more information on the app, its state and goals for the future
def show_concept_screen(prev_frame, root, images):
    clear_frame(prev_frame)

    concept_frame = tk.Frame(root)
    concept_frame.pack(side="top", fill="both", expand=True)
    set_background(concept_frame, images[4])

    concept_label = tk.Label(concept_frame, text="ScrollSense helps you with a lot of things like:\n"
                                                 "- tracking your time on social media\n"
                                                 "- suggests alternative activities\n"
                                                 "- subliminally reducing social media usage \n"
                                                 "- sustainably reducing your screentime\n\n\n"
                                                 "in the future ScrollSense will also have\n"
                                                 "- a journaling section"
                                                 "- a Doomscrolling stopper that pops up after a set amount of time\n"
                                                 "asking you if you are aware of your Doomscrolling,\n"
                                                 "thereby stopping you from getting lost on Social Media\n"
                                                 "Wanna find out more on the idea and \n"
                                                 "concept of this app?\n\n"
                                                 "more information available in my report\n"
                                                 ":)")
    concept_label.place(x=270, y=530, anchor="center")

    exit_button = tk.Button(concept_frame, text="End the demo", command=root.destroy)
    exit_button.place(x=270, y=700, anchor="center")

# This code initiates the main window and loads the pictures.
def run_app():
    root = tk.Tk()
    root.title("ScrollSense")
    root.geometry("540x960")

    intro_bg = Image.open("images/ScrollSenseScreenshot1.jpg")
    warning_bg = Image.open("images/ScrollSenseScreenshot2.jpg")
    usage_bg = Image.open("images/ScrollSenseScreenshot3.jpg")
    instagram_bg = Image.open("images/ScrollSenseScreenshot4.jpg")
    concept_bg = Image.open("images/ScrollSenseScreenshot1.jpg")

    images = [intro_bg, warning_bg, usage_bg, instagram_bg, concept_bg]

    show_intro_screen(root, images)

    root.mainloop()

run_app()