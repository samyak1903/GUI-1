#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
from tkinter import *
def func():
    rlbL.configure(text="Hello Python",font='Times 20 bold')
    rlbL.pack()
root=Tk()
hwL=Label(root,text='Hello World',font='Times 20 bold underline')
hwL.pack()
rlbL=Label(root)
rlbL.pack()
submitB=Button(root,text="Click Me",command=func)
submitB.pack()
exitB=Button(root,text="Exit",command=root.destroy)
exitB.pack()
root.mainloop()
