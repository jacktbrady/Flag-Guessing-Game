import random
import tkinter as tk
from PIL import Image, ImageTk
import os
from unidecode import unidecode
from data.country_mapping import country_mapping
from styles import *
from utils import *

dark_mode = False
guessed_flags = set()

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_styles(root, key_instructions, key_instructions_shift, guess_label, guess_entry, submit_button,
                  feedback_label, answer_label, next_button, play_again_button, score_label, dark_mode)
    update_toggle_button()
    resize_window()


flags = load_flags()
if not flags:
    print("Error: Flags could not be loaded.")
    exit()

total_flags = len(flags)
MIN_WIDTH, MIN_HEIGHT = 800, 600
MIN_HEIGHT_PADDING = 100

def clean_country_name(country_name):
    if len(country_name) == 2 and country_name in country_mapping:
        return country_mapping[country_name]
    else:
        return unidecode(country_name).lower()

def display_flag(flag_filename):
    clear_console()
    image = Image.open(flag_filename)
    image = ImageTk.PhotoImage(image)
    flag_label.configure(image=image)
    flag_label.image = image
    root.update()

def update_percentage():
    if correct_answers.get() > 0:
        percentage = (correct_answers.get() / total_flags) * 100
        percentage_label.config(text=f"Percentage: {percentage:.2f}%")
    else:
        percentage_label.config(text="Percentage: 0.00%")


def resize_window():
    current_width = root.winfo_width()
    current_height = root.winfo_height()
    current_padding = MIN_HEIGHT_PADDING if dark_mode else 0  # Apply padding only in dark mode
    root.geometry(f"{current_width}x{current_height + current_padding}")


def submit_guess(event=None):
    if correct_answers.get() == total_flags:
        return
    guess = guess_entry.get().strip()
    guess = clean_country_name(guess)

    clean_actual_names = clean_country_name(current_flag["name"])

    # Check if the abbreviation has multiple mappings
    if isinstance(clean_actual_names, list):
        if guess.lower() in clean_actual_names:
            feedback_label.config(text="Correct!", fg="green")
            correct_answers.set(correct_answers.get() + 1)
            update_percentage()
            score_label.config(text=f"Score: {correct_answers.get()}/{total_flags}")
        else:
            feedback_label.config(text="Incorrect!", fg="red")
            answer_label.config(text="The correct answers are: " + ', '.join(clean_actual_names), fg="blue")
    else:
        # Remove hyphens for comparison
        if "-" in guess:
            guess_without_hyphen = guess.replace("-", "")
        else:
            guess_without_hyphen = guess

        if guess_without_hyphen.lower() == clean_actual_names.lower():
            feedback_label.config(text="Correct!", fg="green")
            correct_answers.set(correct_answers.get() + 1)
            update_percentage()
            score_label.config(text=f"Score: {correct_answers.get()}/{total_flags}")
        else:
            feedback_label.config(text="Incorrect!", fg="red")
            answer_label.config(text="The correct answer is: " + clean_actual_names, fg="blue")

    if correct_answers.get() == total_flags:
        game_over()
    else:
        submit_button.config(state=tk.DISABLED)
        next_button.config(state=tk.NORMAL)


def game_over():
    clear_console()
    score = correct_answers.get()
    score_label.config(text=f"Game Over! Your final score is: {score}/{total_flags}")
    guess_entry.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)
    next_button.config(state=tk.DISABLED)
    play_again_button.pack(pady=10)

def next_flag(event=None):
    guess_entry.delete(0, tk.END)
    feedback_label.config(text="")
    answer_label.config(text="")
    submit_button.config(state=tk.NORMAL)
    next_button.config(state=tk.DISABLED)
    if flags:
        global current_flag
        current_flag = random.choice(flags)
        flags.remove(current_flag)
        display_flag(current_flag["filename"])
    else:
        game_over()

def next_question(event):
    if event.keysym == "Shift_L" or event.keysym == "Shift_R":
        next_flag()
def update_toggle_button():
    if dark_mode:
        toggle_button.config(image=sun_icon, bd=0, relief=tk.FLAT, highlightthickness=0)
    else:
        toggle_button.config(image=moon_icon, bd=0, relief=tk.FLAT, highlightthickness=0)
    toggle_button_x = 10
    toggle_button_y = 10
    toggle_button.place(x=toggle_button_x, y=toggle_button_y)

def toggle_play_again_button():
    if play_again_button.winfo_ismapped():
        play_again_button.pack_forget()
    else:
        play_again_button.pack(pady=10)

def play_again():
    global flags, total_flags, current_flag
    flags = load_flags()
    if not flags:
        print("Error: Flags could not be loaded.")
        exit()

    total_flags = len(flags)
    correct_answers.set(0)
    score_label.config(text=f"Score: {correct_answers.get()}/{total_flags}")
    update_percentage()  # Update the percentage when starting a new game
    toggle_play_again_button()
    guess_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)
    next_button.config(state=tk.DISABLED)
    next_flag()


root = tk.Tk()
configure_root_style(root)
root.title("Guess the Flags")

moon_image = Image.open("data/moon.png")
sun_image = Image.open("data/sun.png")
moon_image = moon_image.resize((40, 40))
sun_image = sun_image.resize((40, 40))

key_instructions = tk.Label(root, text="Press Enter to submit your guess.")
configure_key_instructions_style(key_instructions)
key_instructions.pack(pady=5)

key_instructions_shift = tk.Label(root, text="Press Shift key for the next question.")
configure_key_instructions_style(key_instructions_shift)
key_instructions_shift.pack(pady=5)

flag_label = tk.Label(root)
configure_flag_label_style(flag_label)
flag_label.pack(pady=10)

guess_frame = tk.Frame(root, bg=get_text_color(dark_mode))
configure_guess_frame_style(guess_frame, padding_bottom=10)
guess_frame.pack(pady=10)


# Create a label for the text "Guess the country:" inside the guess_frame
guess_label_frame = tk.Frame(guess_frame, bg="blue")  # Change "blue" to your desired background color
guess_label_frame.pack(side=tk.LEFT, padx=5)  # Adjust padding as needed

guess_label = tk.Label(guess_label_frame, text="Guess the country: ")
configure_guess_label_style(guess_label, dark_mode=False)  # Set dark_mode=False for light mode appearance
guess_label.pack()

guess_entry = tk.Entry(guess_frame)
configure_guess_entry_style(guess_entry, dark_mode=False)  # Set dark_mode=False for light mode appearance
guess_entry.pack(side=tk.LEFT)

submit_button = tk.Button(guess_frame, text="Submit", command=submit_guess)
configure_submit_button_style(submit_button, dark_mode=False)  # Set dark_mode=False for light mode appearance
submit_button.pack(side=tk.LEFT, padx=10)

feedback_label = tk.Label(root, text="", fg="green")
configure_feedback_label_style(feedback_label, dark_mode=False)  # Set dark_mode=False for light mode appearance
feedback_label.pack(pady=10)

answer_label = tk.Label(root, text="")
configure_answer_label_style(answer_label, dark_mode=False)  # Set dark_mode=False for light mode appearance
answer_label.pack(pady=10)

next_button = tk.Button(root, text="Next", command=next_flag, state=tk.DISABLED)
configure_next_button_style(next_button, dark_mode=False)  # Set dark_mode=False for light mode appearance
next_button.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", command=play_again)
toggle_play_again_button()
correct_answers = tk.IntVar()
correct_answers.set(0)

score_label = tk.Label(root, text=f"Score: {correct_answers.get()}/{total_flags}")
percentage_label = tk.Label(root, text="Percentage: 0.00%")
configure_labels_style(score_label, dark_mode=False)  # Set dark_mode=False for light mode appearance
score_label.pack(pady=10)

update_styles(root, key_instructions, key_instructions_shift, guess_label, guess_entry, submit_button,
              feedback_label, answer_label, next_button, play_again_button, score_label, dark_mode)

current_flag = None
next_flag()
root.bind("<Return>", submit_guess)
root.bind("<KeyPress>", next_question)
root.geometry(f"{MIN_WIDTH}x{MIN_HEIGHT + MIN_HEIGHT_PADDING}")

moon_icon = ImageTk.PhotoImage(moon_image)
sun_icon = ImageTk.PhotoImage(sun_image)

toggle_button_x = guess_label.winfo_x()
toggle_button_y = guess_label.winfo_y() - 50  # Adjust this value to set the desired vertical position
toggle_button = tk.Button(root, image=moon_icon, command=toggle_dark_mode, bd=0, bg="black" if dark_mode else "white")
toggle_button.place(x=toggle_button_x, y=toggle_button_y)

update_toggle_button()

root.mainloop()
