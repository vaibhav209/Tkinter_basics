from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()

root.geometry("300x200+20+10")

def submit():
    Radiobutton.destroy()
    ItemList.destroy()

var = StringVar()
var.set("Radio")

Label(root, text = "What would you like to have sir?",font="lucida 19 bold", justify=LEFT, padx=14).pack()

ItemList = [ 'Pizza', 'Boriyani', 'Fried Rice']
for i, item in enumerate(ItemList):
    Radiobutton(root, text= item, padx=14, variable=var, value= i+1).pack(anchor='w')


b1=Button(text="Submit", command=submit).pack()
# b2=Button(text="Next", command=nextqs).pack()


# continue..................









root.mainloop()