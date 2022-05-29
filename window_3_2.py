#Import the required Libraries
from tkinter import *

#Main
window = Tk()
window.title("Who's Who in Hollywood (Project 7)")
window.configure(background="White")
window.geometry("140x80")

#Create label
Label(window, text="Placeholder for output.", bg="white", fg="black", font="non 10").grid(row=1, column=0)

#Create button
Button(window, text="Start a new search", width=15).grid(row=3, column=0)

window.mainloop()