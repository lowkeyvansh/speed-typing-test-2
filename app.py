import tkinter as tk
from tkinter import messagebox
import time
import random

def setup_window():
    root = tk.Tk()
    root.title("Speed Typing Test")
    root.geometry("600x400")
    return root

def create_text_display(root):
    sentence_label = tk.Label(root, text="", wraplength=550, font=("Helvetica", 14))
    sentence_label.pack(pady=20)
    return sentence_label

def create_input_field(root):
    input_entry = tk.Entry(root, width=80, font=("Helvetica", 14))
    input_entry.pack(pady=20)
    return input_entry

start_time = 0
end_time = 0

def start_timer():
    global start_time
    start_time = time.time()

def end_timer():
    global end_time
    end_time = time.time()

def calculate_wpm(input_text, start_time, end_time):
    elapsed_time = end_time - start_time
    word_count = len(input_text.split())
    wpm = (word_count / elapsed_time) * 60
    return wpm

def start_test(sentence_label, input_entry):
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "The only limit to our realization of tomorrow is our doubts of today."
    ]
    selected_sentence = random.choice(sentences)
    sentence_label.config(text=selected_sentence)
    input_entry.delete(0, tk.END)
    input_entry.bind("<KeyPress>", lambda event: start_timer() if event.keysym == 'Return' else None)

def end_test(sentence_label, input_entry):
    input_text = input_entry.get().strip()
    end_timer()
    wpm = calculate_wpm(input_text, start_time, end_time)
    messagebox.showinfo("Typing Test Result", f"Your typing speed is {wpm:.2f} WPM")

def create_buttons(root, sentence_label, input_entry):
    start_button = tk.Button(root, text="Start Test", command=lambda: start_test(sentence_label, input_entry))
    start_button.pack(pady=10)

    end_button = tk.Button(root, text="End Test", command=lambda: end_test(sentence_label, input_entry))
    end_button.pack(pady=10)

    return start_button, end_button

def main():
    root = setup_window()

    sentence_label = create_text_display(root)
    input_entry = create_input_field(root)
    start_button, end_button = create_buttons(root, sentence_label, input_entry)

    root.mainloop()

if __name__ == "__main__":
    main()
