#Import the required Libraries
from tkinter import *
from tkinter import ttk
from Project_07 import *
from window_3_1 import *



nameOfFstMovie = ""
operator = ""
nameOfSndMovie = ""


def startMoviesWindow():
    #Main
    window = Tk()
    window.title("Who's Who in Hollywood")
    window.configure(background="White")
    window.geometry("530x310")

   

    #Create label
    Label(window, text="Provide the names of two movies either sperated by '&' if you want to retrieve all the actors,\n'|' if you want the actors that have been a part of both movie crews,\nor '^' if you all actors that have been only part of one of the movies.", bg="white", fg="black", font="non 10").grid(row=1, column=0)

    #Create label for movie #1
    Label(window, text="Enter the name of the first movie: ", bg="white", fg="black", font="non 10").grid(row=4, column=0)

   
    #Create entry label for movie #1
    fstInput=Entry(window, width=50, bg="White")
    fstInput.grid(row=5, column=0)

    #Create label for operator
    Label(window, text="\nPick the operator you would like to apply: ", bg="white", fg="black", font="non 10").grid(row=7, column=0)

   

    #Creating dropdown menu
    operator=["&", "|", ","]
    dd=ttk.Combobox(window,values=operator,width=10)
    dd.grid(row=9,column=0,padx=10,pady=10)

    #Create label for movie #2
    Label(window, text="\nEnter the name of the second movie: ", bg="white", fg="black", font="non 10").grid(row=10, column=0)

    

    #Create entry label for movie #2
    sndInput=Entry(window, width=50, bg="White")
    sndInput.grid(row=11, column=0)

    #Needed space (did not know how to create it differently)
    Label(window, text=" ", bg="white", fg="black", font="non 10").grid(row=12, column=0)

    def evaluateInput():
        fstMovie = fstInput.get()
        sndMovie = sndInput.get()
        print("Movie one is: " + str(fstMovie) + "movie two is: " + str(sndMovie))
        
        result = handleOptionA(fstMovie + " | " +sndMovie)
        print("The involved actors are: " + str(result))
        startMoviesResultWindow((result))

        return fstMovie + " | " +sndMovie
    #Create submit button
    Button(window, text="Submit", width=6, command = evaluateInput).grid(row=13, column=0)

    

    window.mainloop()

