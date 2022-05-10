# wfp, 2/29
# run the proj07 demo project
from typing import Dict

#import proj07Demo

dictM = {"" : {""}}


def getActor(inputStr):
    inputArr = inputStr.split(",")

    return inputArr[0]

def getMovies(inputStr):
    inputArr = inputStr.split(",")
    del inputArr[0]
    return inputArr


def addMoviesToDictionary(actor, movies):
    
    keys = dictM.keys()

    for movie in movies:
        if movie in keys:
            newActors = dictM[movie].add(actor)
            dictM.update({movie : newActors })
            print(movie + "is in the set \n")       
        else:
            dictM[movie] = {actor}

   # print("Movies and actors added \n")

def readFile():
    f = open("movies.txt", "r")
    
    for x in f:
        actor = getActor(x)
       # print(actor + "\n")
        movies = getMovies(x)
        #print(str(movies) + "\n")
        addMoviesToDictionary(actor, movies)
        print(dictM)

readFile()