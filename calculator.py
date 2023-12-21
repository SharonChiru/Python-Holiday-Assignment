import tkinter as tk
import tkinter as tk


# the main window for your calculator
root = tk.Tk()
root.title("Simple Calculator")

#Create an Entry widget to display the input and output
entry = tk.Entry(root, width=25, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=5)

# Define functions for digit buttons, arithmetic operation buttons, 
# and the clear/reset button.
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

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
#Create buttons using the Button widget and 
#link them to the functions defined in Step
        # Digits
for i in range(1, 10):
    button = tk.Button(root, text=str(i), padx=20, pady=20, font=('Arial', 14), command=lambda i=i: button_click(i))
    button.grid(row=(i-1)//3 + 1, column=(i-1)%3)

# Zero
zero_button = tk.Button(root, text='0', padx=20, pady=20, font=('Arial', 14), command=lambda: button_click(0))
zero_button.grid(row=4, column=1)

# Arithmetic Operations
operations = ['+', '-', '*', '/' ,  ]
for i, op in enumerate(operations):
    button = tk.Button(root, text=op, padx=25, pady=25, font=('Arial', 14), command=lambda op=op: button_click(op))
    button.grid(row=i+1, column=3)

# Additional Buttons
additional_buttons = [
    ('%', lambda: button_click('%')),
    
]


for i, (text, command) in enumerate(additional_buttons):
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=command)
    button.grid(row=len(operations) + i + 1, column=3)


  

# Clear/Reset
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry)
clear_button.grid(row=4, column=0)

# Equals
equals_button = tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 14), command=calculate)
equals_button.grid(row=4, column=2)


#Finish by starting the Tkinter main loop
root.mainloop()
