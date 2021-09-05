from tkinter import * 

root =Tk()
root.geometry("400x350")

f1 = Frame(root, bg="green", borderwidth=3, relief=RIDGE)
f1.pack(side=RIGHT, anchor=SW )

l = Label(f1, text="SEND", bg="green")
l.pack(padx=50)

f2 = Frame(root, borderwidth=3, bg="grey", relief=RIDGE)
f2.pack(side=LEFT,anchor=SW, fill=X)

l2 = Label(f2, text="Type something here...", bg="white",padx=145)
l2.pack(padx=0)



root.mainloop()