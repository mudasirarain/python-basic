import tkinter as tk
from tkinter import ttk

#window
root = tk.Tk()
root.geometry('250x150')
root.title("my convertor")

#logic
 
def convert():
    x = input_var.get() 
    print(f"this is convert button {x}")
    con = x*100
    output_var.set(con)


#interface
tittle_lable =ttk.Label(root,text="convert meter to cm",font="arial 14 bold",padding='10')
tittle_lable.pack()

input_frame = ttk.Frame(root,padding=10)
input_frame.pack()

input_var = tk.DoubleVar()
entry_convert = ttk.Entry(input_frame, textvariable=input_var)
entry_convert.grid(row=0,column=0)

btn_convert = ttk.Button(input_frame,text="convert",command=convert)
btn_convert.grid(row=0,column=1)

output_var = tk.StringVar()
lbl_output=ttk.Label(root, text="show result", font="arial 14 bold",padding=10,textvariable=output_var)
lbl_output.pack()

root.mainloop()

