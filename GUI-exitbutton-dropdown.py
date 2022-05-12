#from curses import BUTTON_ALT
#from tkinter import *
#For Drop Down the following is needed
#from kinter import ttk

#root = Tk()
#root.title("Learn to Code at Codamy.com")

#Create an exit button, so when you click it, the window will be closed
#https://www.youtube.com/watch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=8
#button_quit = Button(root, text = "Exit Program", command=root.quit)
#button_quit.pack()

#Drop Down Box
#https://www.youtube.com/watch?v=fXotGRP6x4E&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=34
#e.g. ttk.Combobox(search_customers,value = ["Search by...", "Last Name", "E-Mail Address", "Customer ID"])
#drop.current(0)
#drop.grid(row=0, column=2)

#root.mainloop()

# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )

# Change the label text
def show():
	label.config( text = clicked.get() )

# Dropdown menu options
options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Monday" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()
