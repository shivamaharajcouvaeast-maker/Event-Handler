from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)

window.bind("<Buttion-1>",handle_keypress)

def handle_click(event):
    print("\nThe buttion was clicked!")

button = Button(text='Click me')
button.pack()

button.bind('<buttion-1>',handle_click)

window.mainloop()