from tkinter import *

root = Tk()
root.geometry("122x133")

def hello():
    print("Hello Tkinter")


def gui():
    print("This is your Message")

root.title("Welcome to ChatRoom")

f1 = Frame(root, borderwidth=1, bg="grey")
f1.pack(side=LEFT, anchor=SE)

b1= Button(f1, fg="red", text="SEND", command=hello)
b1.pack(side=RIGHT, anchor=SE)


f2 = Frame(root, borderwidth=2, bg="white", relief=RIDGE )
f2.pack(side=RIGHT, anchor=SE)


b2= Button(f1, fg="red", text="Type your message here...", command=gui)
b2.pack(side=RIGHT, anchor=SE)

root.mainloop()






# from tkinter import *

# root=Tk()

# root.geometry("190x135")

# def getvals():
#     print(f"The value of username is {uservalue.get()}")     # You can create also in string from by using F" String
#     print(f"The value of password is {pasvalue.get()}")

# user = Label(root,text="Username")
# pas = Label(root,text="Password")
# user.grid()
# pas.grid(row=1)

# # Vairiable Classes in tkinter
# # BooleanVar, DoubleVar, StringVar

# uservalue= StringVar()
# pasvalue= StringVar()

# userentry = Entry(root,textvariable= uservalue)
# pasentry = Entry(root,textvariable= pasvalue)

# userentry.grid(row=0, column=1)
# pasentry.grid(row=1, column=1)

# Button(text="Submit",command=getvals).grid()

# root.mainloop()



