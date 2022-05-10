# wfp, 2/29
# run the proj07 demo project
from typing import Dict

#import proj07Demo

#Declare globale dictionary
moviesDict = {}

#Ask user what he or she would like to do (two options provided)
userinput1 = int(input("Do you want to get different intersections of actors depending on two movies? Answer with 'Movies.' If you prefer to have the co-actors of an actor displayed, answer with 'Actors.'"))

#Define the two possible answers asked for as variables 
mov_str = ['Movies']
act_str = ['Actors']

#If user wants to continue with 'Movies' further input is needed and therefore requested
userinput2 = int(input("Provide the names of two movies either sperated by '&' if you want to retrieve all the actors, '|' if you want the actors that have been a part of both movie crews, or '^' if you all actors that have been only part of one of the movies."))

#If user wants to continue with 'Actors' further input is needed and therefore requested
userinput3 = int(input("Provide the names of two actors (first and last name). Seperate the actor's names by a comma."))

#Check with an if-function what the user would like to do next and provide the output
print(userinput1)
if userinput1 = mov_str
    print(userinput2)

else

#getCoactors()



#Function that takes an input line and retures the actor
def getActor(inputStr):
    #Split input line by a "," and convert it into an array
    inputArr = inputStr.split(",")
    
    #Return the first element of the array which is the actor
    return inputArr[0]

#Function that takes an input line and retures all movies in an array
def getMovies(inputStr):
    #Split input line by a ", " and convert it into an array, thereby already eliminate the space after the ","
    inputArr = inputStr.split(", ")
    #Erase the Actor which is the first element of the array
    del inputArr[0]
    movies = []
    #Loop through the array and earse all \n etc.
    for movie in inputArr:
        movies.append(movie.strip())
    return movies
    
    



def addMoviesToDictionary(actor, movies):
    #Get all the keys from the dictionary    
    keys = moviesDict.keys()

    #Loop through all movies that are in the passed line
    for movie in movies:
        #Check if the current movie was already added to the dictionary
        if movie in keys:
            #If yes, add the passed actor to the set of actors of the current movie
            moviesDict[movie].add(actor)
        else:
            #If not, add the movie to the dictionary with the passed actor in a set
            moviesDict[movie] = {actor}



def readFile():
    #read the file
    f = open("movies.txt", "r")
    
    #Go through each line in the file and add the data to the dictionary
    for x in f:
        actor = getActor(x)
        movies = getMovies(x)
        addMoviesToDictionary(actor, movies)
        
    print(moviesDict)

readFile()