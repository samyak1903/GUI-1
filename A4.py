#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.

from tkinter import *
def func():
    nmL.configure(text=nmE.get(),font='Times 20 ')
    nmL.pack()
root=Tk()
hwL=Label(root,text='Enter your name:',font='Times 20 bold')
hwL.pack()
nmE=Entry(root)
nmE.pack()
submitB=Button(root,text="Submit",command=func)
submitB.pack()
exitB=Button(root,text="Exit",command=root.destroy)
exitB.pack()
nmL=Label(root)
nmL.pack()
root.mainloop()
