from tkinter import *

root = Tk()

#Create input box
#Change size of input box: width=50
#Change color of input box: bg="blue"
#Change text color in input box: fg="white"
e = Entry(root)
e.pack()

#Put some default text inside of the text box
e.insert(0, "Enter your Name: ")

#e.get to do something with what has been written in the input box
def myClick():
    myLabel = Label(root, text = "Hallo " + e.get())
    myLabel.pack()

#Disables button: state = DISABLED 
#Changes size of button: padx=50, pady=50
MyButton = Button(root, text = "Enter Your Name", command = myClick)
MyButton.pack()

root.mainloop()