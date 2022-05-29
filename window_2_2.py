#Import the required Libraries
from tkinter import *
from Project_07 import *
from window_3_1 import *

nameOfActor = ""

def startActorsWindow():

    #Main
    window = Tk()
    window.title("Who's Who in Hollywood (Project 7)")
    window.configure(background="White")
    window.geometry("400x70")

    #Create label
    Label(window, text="Enter an actor's (first and last) name to display his or her co-actors.", bg="white", fg="black", font="non 10").grid(row=1, column=0)

    #Create entry label
    fstInput=Entry(window, width=50, bg="White")
    fstInput.grid(row=2, column=0)

    def evaluateInput():
        actorName = fstInput.get()
        

        result = handleOptionB(actorName)

        startMoviesResultWindow(result)

        



    Button(window, text="Submit", width=6, command = evaluateInput).grid(row=13, column=0)
    window.mainloop()