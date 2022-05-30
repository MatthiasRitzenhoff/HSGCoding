##This class allows user to use the programm from the terminal

from services import *




#Function that asks for the user imput, calls the corresponding functions to generate the output and prints the output to the user
def handleUserInput():
    

    #Ask user what he or she would like to do (two options provided)
    menuSelection = str(raw_input("Do you want to get different intersections of actors depending on two movies? Answer with 'Movies.' If you prefer to have the co-actors of an actor displayed, answer with 'Actors.'"))
    print(menuSelection)
    if menuSelection == "Movies":
        #If user wants to continue with 'Movies' further input is needed and therefore requested
        movies = str(raw_input("Provide the names of two movies either sperated by '&' if you want to retrieve all the actors, '|' if you want the actors that have been a part of both movie crews, or '^' if you all actors that have been only part of one of the movies."))
        
        #Seperate the user input into the three parts First Movie, Operator, Second Movie
        inputArr = inputArr = movies.split(" ")
        fstMovie = inputArr[0]
        sndMovie = inputArr[2]
        operator = inputArr[1]

        print("The involved actors are: " + str(handleOptionA(fstMovie, operator, sndMovie)))
        
    elif menuSelection == "Actors":
        #If user wants to continue with 'Actors' further input is needed and therefore requested
        actor = str(raw_input("Enter an actor's (first and last) name to display his or her co-actors."))
        print(actor + " acted togehter with " + str(handleOptionB(actor)))
    else:
        #If the input was incorrect notfy the user and call the function again
        print("Invalied input, please follow the instructions. \n")
        handleUserInput()




#Main function that is called when the programm is run
def main ():
    #Call a function to ask the user for the input and handle the results
    handleUserInput()


main()



