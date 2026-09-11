import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        file = open(filepath, "r")
        text_editor.delete("1.0", tk.END)
        text_editor.insert(tk.END, file.read())
        file.close()

def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath:
        file = open(filepath, "w")
        file.write(text_editor.get("1.0", tk.END))
        file.close()

root = tk.Tk()
root.title("Letter Writing Application")

open_button = tk.Button(root, text="Open Letter", command=open_file)
open_button.grid(row=0, column=0, padx=5, pady=5)

save_button = tk.Button(root, text="Save As...", command=save_file)
save_button.grid(row=0, column=1, padx=5, pady=5)

text_editor = tk.Text(root, width=60, height=20)
text_editor.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
