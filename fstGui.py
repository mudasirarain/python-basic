#rom tkinter import*

#root = Tk()
#Label1 = Label(root, text="this is my first lable.......")
#Label2 = Label(root, text = "this is my second lable......").grid(row=0, column=1)

#labell.pack()
#Label1.grid(row=0,column=0)


#root.mainloop()

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()