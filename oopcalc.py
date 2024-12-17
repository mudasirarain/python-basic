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



    def btns(self, panel, t, r, c):
        btn = ttk.Button(panel, text=t, command=lambda val=t: self.showNum(val))
        btn.grid(row=r, column=c)

# Run the calculator
Calc('My Calculator', 250, 300)
