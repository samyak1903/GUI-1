#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
from tkinter import *
def func():
    hwL.configure(text="Hello Python",font='Times 20 bold')
    hwL.pack()
root=Tk()
frame1=Frame(root,bg='black')
frame1.pack()
hwL=Label(frame1,text='Hello World',font='Times 20 bold underline')
hwL.pack()
submitB=Button(frame1,text="Click Me",command=func)
submitB.pack()
exitB=Button(frame1,text="Exit",command=root.destroy)
exitB.pack()
root.mainloop()
