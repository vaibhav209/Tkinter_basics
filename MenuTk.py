from tkinter import * 
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("400x300")
root.title("Untitled - Menu and Submenu")

def myfile():
    print("The menu with submenu is called")

def help():
    print('I can help you')
    tmsg.showinfo("Help", "I will help you with this GUI")

def rate():
    value= tmsg.askquestion("Rate it!", "Was good experience?")
    if value == "yes":
        msg = "Great. Rate us on app store please!"
    else:
        msg = "Tell us what went wrong, We will call you soon"
    tmsg.showinfo("Experience", msg)    
    
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfile)
# mymenu.add_command(label="Edit", command=myedit)
# mymenu.add_command(label="Format", command=myformat)
# mymenu.add_command(label="View", command=myview)
# mymenu.add_command(label="Help", command=myhelp)
# mymenu.add_command(label="Exit", command=quit)

# root.configure(menu=mymenu)  #File
# root.configure(menu=mymenu)  #Edit
# root.configure(menu=mymenu)  #Format
# root.configure(menu=mymenu)  #View
# root.configure(menu=mymenu)  #Help



Mainmenu = Menu(root)



m1 = Menu(Mainmenu,tearoff=0)                             # If you don't want a tearoff in submenu then use it 
m1.add_command(label="New", command=myfile)
m1.add_command(label="Open...", command=myfile)
m1.add_command(label="Save", command=myfile)
m1.add_command(label="Save As...", command=myfile)
m1.add_separator()
m1.add_command(label="Page Setup...", command=myfile)
m1.add_command(label="Print...", command=myfile)
m1.add_separator()
m1.add_command(label="Exit", command=quit)

root.config(menu=Mainmenu)

Mainmenu.add_cascade(label="File", menu=m1)



m2 = Menu(Mainmenu,tearoff=0)                              
m2.add_command(label="Cut", command=myfile)
m2.add_command(label="Copy", command=myfile)
m2.add_command(label="Paste", command=myfile)
m2.add_command(label="Replace", command=myfile)
m2.add_separator()
m2.add_command(label="Go To...", command=myfile)
m2.add_command(label="Select All", command=myfile)

root.config(menu=Mainmenu)

Mainmenu.add_cascade(label="Edit", menu=m2)


m3 = Menu(Mainmenu,tearoff=0)                              
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us...", command=rate)

Mainmenu.add_cascade(label="Help", menu=m3)

root.config(menu=Mainmenu)


entry = Text(root, bg="white", font="comicsansms 13 bold")
entry.pack(padx=5, pady=5)



root.mainloop()