##This class provides the window when the user selected the second option

#Import the required Libraries
from tkinter import *
from tkinter import ttk
from services import *
from result_Window import *


def startMoviesWindow():
    #Create main window
    window = Tk()
    window.title("Who's Who in Hollywood")
    window.configure(background="White")
    window.geometry("800x450")


    #Create label
    Label(window, text="Provide the names of two movies either and one of the following operators: \n 1.)'&' if you want to retrieve the actors that played in both movies\n 2.)'|' if you want to retriev the actors that plaed in either of the two movies,\n3.)'^' if you all actors that have been only part of one of the movies.\n", bg="white", fg="black", font="non 10").grid(row=1, column=0)

    #Crete label to announce that all Movies are displayed
    Label(window, text="These are all avaiable Movies:", bg="white", fg="black", font="non 10").grid(row=3, column=0)

    #Create a lable to display all movies
    Label(window, text=getAllMovies() + "\n", bg="white", fg="black", font="non 10").grid(row=4, column=0)


    #Create label for movie #1
    Label(window, text="Enter the name of the first movie: ", bg="white", fg="black", font="non 10").grid(row=5, column=0)

   
    #Create entry label for movie #1
    fstInput=Entry(window, width=50, bg="White")
    fstInput.grid(row=6, column=0)

    #Create label for operator
    Label(window, text="\nPick the operator you would like to apply: ", bg="white", fg="black", font="non 10").grid(row=7, column=0)

    #Creating dropdown menu
    operator=["&", "|", "^"]
    dd=ttk.Combobox(window,values=operator,width=10)
    dd.grid(row=9,column=0,padx=10,pady=10)

    #Create label for movie #2
    Label(window, text="\nEnter the name of the second movie: ", bg="white", fg="black", font="non 10").grid(row=10, column=0)

    #Create entry label for movie #2
    sndInput=Entry(window, width=50, bg="White")
    sndInput.grid(row=11, column=0)

    #Needed space (did not know how to create it differently)
    Label(window, text=" ", bg="white", fg="black", font="non 10").grid(row=12, column=0)

    #Function that is called the button is pressed and handels the user input
    def evaluateInput():
        #Get input from input fields
        fstMovie = fstInput.get()
        sndMovie = sndInput.get()
        selOperator = dd.get()
        
        #Crate and format the output strings
        resultStr = "The result of " + fstMovie + " " + selOperator + " " + sndMovie + " is:\n"
        result = handleOptionA(fstMovie, selOperator, sndMovie)
        
        startMoviesResultWindow(resultStr, result)
        

    #Create submit button
    Button(window, text="Submit", width=6, command = evaluateInput).grid(row=13, column=0)

    

    window.mainloop()

