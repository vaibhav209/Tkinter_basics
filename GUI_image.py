
from tkinter import *
import tkinter
from PIL import Image, ImageTk

image_root = Tk()

image_root.geometry("600x400")

# photo = PhotoImage(file="nature.png")

# For jpg Image

image = Image.open("temp1.jpg")
photo = ImageTk.PhotoImage(image)


temp_label = Label(image=photo)
temp_label.pack()                     # You want to show the image in your GUI then it is very important to pack the label

image_root.mainloop()





Label & Packs in Tkinter

from tkinter import *
from tkinter.font import BOLD, ITALIC


root = Tk()

root.geometry("300x250")

root.title("Learning GUI Tutorial")

# # Important Label Option
# # Text - Adds the text
# # bd - Background
# # fg - Foreground 
# # Font - sets the font
# # 1. font=("comicsansms",15,"italic")
# # 2. font="comicsansms 15 italic"
# # Padx - x padding
# # Pady - y padding
# # Relief - Border styling - SUNKEN, RAISED, GROOVE,RIDGE


title_label = Label(text= '''
Google LLC is an American multinational technology company that specializes in Internet-related services and products, \nwhich include online advertising technologies, a search engine, cloud computing, software, and hardware. \nIt is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple. \nGoogle was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. \nTogether they own about 14% of its publicly-listed shares and control 56% of the stockholder voting power through super-voting stock. \nThe company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. \nGoogle is Alphabet's largest subsidiary and is a holding company for Alphabet's Internet properties and interests. \nSundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet.''', bg ="gray", fg="white", padx=12, pady=20, font="comicsansms 9 bold", borderwidth=3, relief=RAISED
)

# # Important Pack in Option
# # Anchor = nw (North West)
# # side = top, bottom, left, right

# # Fill    #Fill=X is fill the x axis, and also same for the fill=Y
# # Padx
# # Pady

title_label.pack(side= BOTTOM, anchor=SW,fill=X)


title_label.pack(side= LEFT,fill=Y, padx=22, pady=33)

root.mainloop()

# """""""

## EXERCISE ##
## To make "Ready" strip in bottom on GUI window ##

# """"""""""""""""""""""""
from tkinter import *

root = Tk()

root.geometry("500x400")

label = Label(text='''READY''', bg="yellow", fg="black", font="comicsansm 15 italic", )

label.pack(side=BOTTOM, fill=X, pady=5)

root.mainloop()

# """""""""""""""""""""""""

# """"""""""""""""""""""

# # Canvas Widgets in Tkinter

# from tkinter import *

# root =Tk()

# canvas_width = 800
# canvas_height = 400

# root.geometry(f"{canvas_width}x{canvas_height}")

# can_widget = Canvas(root, width=canvas_width,height=canvas_height)
# can_widget.pack()

# # The line goes the point x1, y1 to x2, y2
# can_widget.create_line(0,0,800,400, fill='red')
# can_widget.create_line(0,400,800,0, fill='red')


# # Rectangle specified in this parameter
# can_widget.create_rectangle(3,5,700,300)

# # you can create text at any where
# can_widget.create_text(400,200, text="python")

# can_widget.create_oval(344,230,450,350)

# root.mainloop()

# """"""""""""""""""""""



## Events in Tkinter

from tkinter import *

def clicked(event):
    print(f"button is click now{event.x},{event.y}")

root = Tk()

root.title("Events in Tkinter")
root.geometry("500x500")

widget = Button(root, text='Click me please')
widget.pack()

widget.bind('<Button-1>', clicked)
widget.bind('<Double-1>', quit)


root.mainloop()