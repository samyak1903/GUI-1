#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
from tkinter import *
root=Tk()
hwL=Label(root,text='Hello World',font='Times 20 bold underline')
hwL.pack()
exitB=Button(root,text="Exit",command=root.destroy)
exitB.pack()
root.mainloop()
