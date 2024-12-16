# 1. Create a simple Python program and make an executable (Total 20 points) 
# Design and implement a simple calculator with a GUI interface 
# to perform just the following functions listed after your first name initial. 

# First name initial A-F: sine, cosine, clear (one digit/char at a time), all clear. 
# First name initial G-M: Hex add, hex subtract, clear (one digit/char at a time), all clear. 
# First name initial N-Z: Octo add, octo subtract, clear (one digit/char at a time), all clear. 

# Once you proved that the program is working in an IDE (10 points), 
# make an executable for users to click on that executable to invoke the calculator program (10 points)

# First name initial: J => Hex add, hex subtract, clear (one digit/char at a time), all clear. 

import tkinter as tk
from tkinter import messagebox

def hex_add():
    try:
        num1 = int(entry1.get(), 16)  # Convert first input to integer (base 16)
        num2 = int(entry2.get(), 16)  # Convert second input to integer (base 16)
        result = hex(num1 + num2)  # Add and convert the result back to hexadecimal
        result_label.config(text=f"Result: {result[2:].upper()}")  # Display the result without '0x'
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid hexadecimal values.")

def hex_subtract():
    try:
        num1 = int(entry1.get(), 16)
        num2 = int(entry2.get(), 16)
        result = hex(num1 - num2)
        result_label.config(text=f"Result: {result[2:].upper()}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid hexadecimal values.")

def clear_digit():
    current = entry1.get()
    if current:
        entry1.delete(len(current)-1, tk.END)

def all_clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Set up the main window
root = tk.Tk()
root.title("Hexadecimal Calculator")

# Input fields for hexadecimal numbers
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=20)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Buttons for operations
add_button = tk.Button(root, text="Add", command=hex_add)
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="Subtract", command=hex_subtract)
subtract_button.grid(row=1, column=1, padx=5, pady=5)

clear_digit_button = tk.Button(root, text="Clear One Digit", command=clear_digit)
clear_digit_button.grid(row=2, column=0, padx=5, pady=5)

all_clear_button = tk.Button(root, text="All Clear", command=all_clear)
all_clear_button.grid(row=2, column=1, padx=5, pady=5)

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()
