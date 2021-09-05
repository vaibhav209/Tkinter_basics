from tkinter import *

root=Tk()
root.geometry("350x250")
root.title("This is my scroll bar")

# For connecting scrollbar to widget
# 1. Widget(yscrollcommand = scrollbar.set)
# 2. Scrollbar.config(command=widget.yview)

scrollbar= Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)



Tb=Text(root, yscrollcommand = scrollbar.set)
Tb.pack()

scrollbar.config(command=Tb.yview)

# statusvar = StringVar()
# statusvar.set("A ChatBot created by Vaibhav")

# sbar = Label(root, textvariable=statusvar, relief = RIDGE)
# sbar.pack(side=TOP, fill=X)
# root.mainloop()