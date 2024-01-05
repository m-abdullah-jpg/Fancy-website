import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(button_value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for displaying and entering numbers
entry = tk.Entry(window, width=20, font=("Arial", 14), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Special buttons
tk.Button(window, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
tk.Button(window, text="AC", width=5, height=2, command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val+1)

# Bind the Enter key to the calculate function
window.bind('<Return>', lambda event=None: calculate())

# Run the main loop
window.mainloop()
