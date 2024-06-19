import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
            messagebox.showerror("Error", "Invalid Expression")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# StringVar to store and display the input and output
screen_var = tk.StringVar()

# Entry widget to display input and output
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
screen.grid(row=0, column=0, columnspan=4)

# Button text
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons in grid
row, col = 1, 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font="lucida 15 bold", padx=20, pady=15)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make the grid cells expand proportionally
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i+1, weight=1)

# Run the main event loop
root.mainloop()
