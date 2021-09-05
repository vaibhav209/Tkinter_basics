#### STATUS BAAR in TKinter GUI ####


from tkinter import *

root = Tk()
root.geometry("380x400")
statusvar = StringVar()
statusvar.set("This is me created by Vaibhav")

sbar = Label(root, textvariable=statusvar, relief = RIDGE)
sbar.pack(side=TOP, fill=X)


root.mainloop()
