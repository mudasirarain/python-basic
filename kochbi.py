# import tkinter as tk

# # Function to update the display based on button clicks
# def button_click(value):
#     current = entry.get()
#     entry.delete(0, tk.END)  # Clear the current display
#     entry.insert(tk.END, current + value)  # Insert the clicked value

# # Function to evaluate the expression and display the result
# def evaluate():
#     try:
#         result = eval(entry.get())  # Use eval to evaluate the expression
#         entry.delete(0, tk.END)  # Clear the display
#         entry.insert(tk.END, str(result))  # Show the result
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # Function to clear the display
# def clear():
#     entry.delete(0, tk.END)

# # Create the main window
# root = tk.Tk()
# root.title("Calculator")

# # Create an entry widget (display)
# entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
# entry.grid(row=0, column=0, columnspan=4)

# # Button layout
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
# ]

# # Create buttons and add them to the grid
# for (text, row, col) in buttons:
#     if text == 'C':
#         tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=clear).grid(row=row, column=col)
#     elif text == '=':
#         tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=evaluate).grid(row=row, column=col)
#     else:
#         tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=lambda t=text: button_click(t)).grid(row=row, column=col)

# # Run the main loop
# root.mainloop()
















import tkinter as tk
from tkinter import ttk

class Calc(tk.Tk):
    def __init__(self, title, w, h):
        super().__init__()
        self.title(title)
        self.geometry(f'{w}x{h}')
        self.interface()
        self.mainloop()

    def interface(self):
        self.screen_var = tk.StringVar()
        screen = ttk.Entry(master=self, font="arial 14", textvariable=self.screen_var)
        screen.pack(side="top", fill="x", pady=10)
    
        btnPanel = ttk.Frame(self)
        btnPanel.pack()

        # Create number and operation buttons
        x = 0
        for i in range(0, 3):
            for j in range(0, 3):
                x = x + 1
                self.btns(btnPanel, x, i, j)

        # Create operator buttons
        self.btns(btnPanel, "+", 0, 3)
        self.btns(btnPanel, "*", 1, 3)
        self.btns(btnPanel, "/", 2, 3)
        self.btns(btnPanel, "-", 3, 3)
        self.btns(btnPanel, "0", 3, 0)

        # Add Cancel and Equal buttons
        self.cancel_button(btnPanel)
        self.equal_button(btnPanel)

    def showNum(self, x):
        calc = self.screen_var.get()
        calc = calc + str(x)
        self.screen_var.set(calc)

    def cancel_button(self, panel):
        cancel_btn = ttk.Button(panel, text="Cancel", command=self.clear_screen)
        cancel_btn.grid(row=3, column=1)

    def equal_button(self, panel):
        equal_btn = ttk.Button(panel, text="=", command=self.calculate_result)
        equal_btn.grid(row=3, column=2)

    def clear_screen(self):
        self.screen_var.set("")

    def calculate_result(self):
        try:
            expression = self.screen_var.get()
            result = str(eval(expression))  # Evaluate the expression entered
            self.screen_var.set(result)
        except Exception as e:
            self.screen_var.set("Error")  # In case of an invalid expression

    def btns(self, panel, t, r, c):
        btn = ttk.Button(panel, text=t, command=lambda val=t: self.showNum(val))
        btn.grid(row=r, column=c)

# Run the calculator
Calc('My Calculator', 250, 300)
