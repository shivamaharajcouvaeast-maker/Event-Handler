import tkinter as tk

def greet_participant():
    name = name_entry.get()
    output_text.delete("1.0", tk.END)
    welcome_message = f"Welcome to the workshop, {name}!\n\nThank you for checking in.\nWe hope you have an incredible learning experience today!"
    output_text.insert(tk.END, welcome_message)

root = tk.Tk()
root.title("Workshop Participant Greeting")
root.geometry("600x450")

title_label = tk.Label(root, text="Workshop Participant Greeting", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Please enter your name below to complete your registration:", font=("Arial", 11))
instruction_label.pack(pady=10)

name_entry = tk.Entry(root, font=("Arial", 12), width=35)
name_entry.pack(pady=10)

check_in_button = tk.Button(root, text="Complete Check-In", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", padx=15, pady=5, command=greet_participant)
check_in_button.pack(pady=20)

output_text = tk.Text(root, font=("Arial", 11), width=50, height=8, wrap=tk.WORD)
output_text.pack(pady=15)

root.mainloop()
