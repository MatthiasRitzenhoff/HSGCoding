##Class that is being called when the user wants to use the GUI

#Import the required Libraries
from tkinter import *
from window_Movies import *
from window_Actors import *


#Main function that is called when the program is being started
def main():
    #Create the main window
    window = Tk()
    window.title("Who's Who in Hollywood")
    window.configure(background="White")
    
    
    #Create label
    Label(window, text="Do you want to get different intersections of actors depending on two movies? Answer with 'Movies.' If you prefer to have the co-actors of an actor displayed, answer with 'Actors.'", bg="white", fg="black", font="non 10").grid(row=1, column=0)

    #Create buttons
    Button(window, text="Movies", width=6, command=startMoviesWindow).grid(row=3, column=0)
    Button(window, text="Actors", width=6, command=startActorsWindow).grid(row=4, column=0)

    window.mainloop()

main()
