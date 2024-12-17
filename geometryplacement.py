from tkinter import*

main = Tk()
main.geometry('600x600')
main.title("Geometry intro")
#frame1 = Frame(main,width=300,hight=500)

mylable = Label(main, text="lable heading", bg='orange',fg="black",padx=10,pady=10)

#mylable.pack(side="left",fill=Y)
#mylable.pack(anchor="sw")

mylable.place(x=23,y=34,relheight=1,relwidth=0.3)

main.mainloop()