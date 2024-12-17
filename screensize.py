from tkinter import*
root=Tk()

root.geometry('400x400')
root.minsize(200,100)

loginhaeding = Label(text="login form",fg="dark blue",bg="grey",font="forte 12 bold",padx=7,pady=15)

iblpassword = Label(text="password").grid(row=2,column=0)
txtusername = Text(height=1, width=24).grid(row=2,column=2)
iblausername = Label(text="username").grid(row=3,column=0)
txtusername = Text(height=1, width=24).grid(row=3,column=2)

btnlogin = Button(text="login").grid(row=5, column=1)

loginhaeding.grid(row=0,column=1)
root.mainloop()