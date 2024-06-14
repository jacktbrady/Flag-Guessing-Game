# styles.py
import tkinter as tk

def get_text_color(dark_mode):
    return "black" if dark_mode else "white"

def reverse_get_text_color(dark_mode):
    return "white" if dark_mode else "black"

def configure_guess_frame_style(frame, padding_bottom=0, dark_mode=False):
    frame.config(bg="black" if dark_mode else "white", bd=0, highlightthickness=2, highlightbackground=reverse_get_text_color(dark_mode), pady=padding_bottom)

def configure_root_style(root, dark_mode=False):
    root.geometry("400x500")
    root.configure(bg=get_text_color(dark_mode))

def configure_labels_style(label, dark_mode=False):
    label.config(font=("Helvetica", 12), bg="black" if dark_mode else "white", fg="white" if dark_mode else "black")

def configure_key_instructions_style(label, dark_mode=False):
    label.config(font=("Helvetica", 12), fg="gray" if dark_mode else "black", bg="black" if dark_mode else "white")

def configure_flag_label_style(label):
    label.config(pady=10)

def configure_guess_label_style(label, dark_mode=False):
    label.config(font=("Helvetica", 14), bg=get_text_color(dark_mode))

def configure_guess_entry_style(entry, dark_mode=False):
    entry.config(font=("Helvetica", 14), bg="black" if dark_mode else "white",
                 fg="white" if dark_mode else "black",
                 insertbackground="white" if dark_mode else "black", bd=0, relief=tk.FLAT)

def configure_submit_button_style(button, dark_mode=False):
    button.config(font=("Helvetica", 12), fg="white" if dark_mode else "black", bg="black" if dark_mode else "SystemButtonFace",
                  bd=1, relief=tk.RAISED)

def configure_feedback_label_style(label, dark_mode=False):
    label.config(fg="green", font=("Helvetica", 16), bg="black" if dark_mode else "white")

def configure_answer_label_style(label, dark_mode=False):
    label.config(fg="black", font=("Helvetica", 12), bg="black" if dark_mode else "white")

def configure_next_button_style(button, dark_mode=False):
    button.config(font=("Helvetica", 12), fg="white" if dark_mode else "black", bg="black" if dark_mode else "SystemButtonFace",
                  bd=1, relief=tk.RAISED)

def configure_play_again_button_style(button, dark_mode=False):
    button.config(font=("Helvetica", 12), fg="white" if dark_mode else "black", bg="black" if dark_mode else "SystemButtonFace",
                  bd=1, relief=tk.RAISED)

def configure_labels_style(score_label, dark_mode=False):
    score_label.config(fg="white" if dark_mode else "black", bg="black" if dark_mode else "white")

def dark_mode_styles(root, key_instructions, key_instructions_shift, guess_label, guess_entry, submit_button,
                     feedback_label, answer_label, next_button, play_again_button, score_label):
    configure_root_style(root, dark_mode=True)
    configure_labels_style(key_instructions, dark_mode=True)
    configure_labels_style(key_instructions_shift, dark_mode=True)
    configure_labels_style(guess_label, dark_mode=True)
    configure_guess_entry_style(guess_entry, dark_mode=True)
    configure_submit_button_style(submit_button, dark_mode=True)
    configure_feedback_label_style(feedback_label, dark_mode=True)
    configure_answer_label_style(answer_label, dark_mode=True)
    configure_next_button_style(next_button, dark_mode=True)
    configure_play_again_button_style(play_again_button, dark_mode=True)
    configure_labels_style(score_label, dark_mode=True)

def default_styles(root, key_instructions, key_instructions_shift, guess_label, guess_entry, submit_button,
                   feedback_label, answer_label, next_button, play_again_button, score_label):
    configure_root_style(root, dark_mode=False)
    configure_labels_style(key_instructions, dark_mode=False)
    configure_labels_style(key_instructions_shift, dark_mode=False)
    configure_labels_style(guess_label, dark_mode=False)
    configure_guess_entry_style(guess_entry, dark_mode=False)
    configure_submit_button_style(submit_button, dark_mode=False)
    configure_feedback_label_style(feedback_label, dark_mode=False)
    configure_answer_label_style(answer_label, dark_mode=False)
    configure_next_button_style(next_button, dark_mode=False)
    configure_play_again_button_style(play_again_button, dark_mode=False)
    configure_labels_style(score_label, dark_mode=False)

def update_styles(root, key_instructions, key_instructions_shift, guess_label, guess_entry, submit_button,
                  feedback_label, answer_label, next_button, play_again_button, score_label, dark_mode):
    print("Updating styles. Dark Mode:", dark_mode)  # Added print statement
    if dark_mode:
        dark_mode_styles(root, key_instructions, key_instructions_shift, guess_label, guess_entry, submit_button,
                         feedback_label, answer_label, next_button, play_again_button, score_label)
    else:
        default_styles(root, key_instructions, key_instructions_shift, guess_label, guess_entry, submit_button,
                       feedback_label, answer_label, next_button, play_again_button, score_label)
