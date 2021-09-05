from tkinter import *
import tkinter



first_root = Tk()

#Minsize Maxsize and Geometry

# Width x Height
first_root.geometry("600x550")

# width , height
first_root.minsize(300,200)

# width , height
first_root.maxsize(1200,300)

#Label

mylabel = Label(text="This is your first label in GUI")
mylabel.pack()
first_root.mainloop()




#733x434

second = Tk()

second.geometry("733x434")

second.mainloop()





