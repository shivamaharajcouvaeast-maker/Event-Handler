import tkinter as tk

def press_key(digit):
    pin_entry.insert(tk.END, digit)

def clear_pin():
    pin_entry.delete(0, tk.END)

def update_status():
    account = acc_entry.get()
    pin = pin_entry.get()
    output_text.delete("1.0", tk.END)
    summary_message = f"Account Number: {account}\nPIN Status: Successfully Configured\nSECURE DATA ENCRYPTED"
    output_text.insert(tk.END, summary_message)

root = tk.Tk()
root.title("ATM PIN Setup Interface")
root.geometry("500x550")

details_frame = tk.Frame(root, bd=3, relief="raised")
details_frame.place(x=30, y=20, width=440, height=80)

acc_label = tk.Label(details_frame, text="Account Number:")
acc_label.pack(side="left", padx=10)

acc_entry = tk.Entry(details_frame, width=25)
acc_entry.pack(side="left", padx=10)

keypad_frame = tk.Frame(root, bd=3, relief="sunken")
keypad_frame.place(x=140, y=120, width=220, height=230)

pin_entry = tk.Entry(keypad_frame, show="*", justify="center", font=("Arial", 14))
pin_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    'C', '0'
]

row_idx = 1
col_idx = 0

for btn_text in buttons:
    if btn_text == 'C':
        btn = tk.Button(keypad_frame, text=btn_text, width=5, height=2, command=clear_pin)
    else:
        btn = tk.Button(keypad_frame, text=btn_text, width=5, height=2, command=lambda t=btn_text: press_key(t))
        
    btn.grid(row=row_idx, column=col_idx, padx=5, pady=5)
    
    col_idx += 1
    if col_idx > 2:
        col_idx = 0
        row_idx += 1

submit_btn = tk.Button(root, text="Confirm & Save PIN", command=update_status)
submit_btn.place(x=185, y=370, width=130, height=35)

output_text = tk.Text(root, width=50, height=5)
output_text.place(x=50, y=430, width=400, height=90)

root.mainloop()
