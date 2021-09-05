from tkinter import *
import time
import os

root=Tk()
root.geometry("1150x600")
icon = PhotoImage(file = 'digital.png')
root.iconphoto(False, icon)
root.title("A Python Based Digital Clock")
root.config(background="yellow")
# root.resizable(0,0)


Hlabel=(root, text="12", font="comicsansms 13 bold", bg="red", fg="white")
Hlabel.place(x=400, y=300, width=150, height=150)






root.mainloop()