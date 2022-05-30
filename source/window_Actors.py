##This class provides Window when the user selected the second optionen

#Import the required Libraries
from tkinter import *
from services import *
from result_Window import *


def startActorsWindow():

    #Creat the main window
    window = Tk()
    window.title("Who's Who in Hollywood")
    window.configure(background="White")
    window.geometry("700x200")

    #Create label
    Label(window, text="Enter an actor's (first and last) name to display his or her co-actors.", bg="white", fg="black", font="non 10").grid(row=1, column=0)

    #Crete label to announce that all Movies are displayed
    Label(window, text="\nThese are all avaiable Actors:", bg="white", fg="black", font="non 10").grid(row=2, column=0)

    #Create a lable to display all movies
    Label(window, text=getAllActors() + "\n", bg="white", fg="black", font="non 10").grid(row=3, column=0)


    #Create entry label
    fstInput=Entry(window, width=50, bg="White")
    fstInput.grid(row=4, column=0)

    #Function that is called the button is pressed and handels the user input
    def evaluateInput():
        #Get data from the input fields
        actorName = fstInput.get()

        #Create and format output strings
        resultStr = actorName + "'s co-actors are: \n"
        result = handleOptionB(actorName)

        startMoviesResultWindow(resultStr, result)

    Button(window, text="Submit", width=6, command = evaluateInput).grid(row=13, column=0)
    window.mainloop()