#Import the required Libraries
from tkinter import *

#Main
window = Tk()
window.title("Who's Who in Hollywood (Project 7)")
window.configure(background="White")
window.geometry("400x70")

#Create label
Label(window, text="Enter an actor's (first and last) name to display his or her co-actors.", bg="white", fg="black", font="non 10").grid(row=1, column=0)

#Create entry label
textentry=Entry(window, width=50, bg="White")
textentry.grid(row=2, column=0)

window.mainloop()