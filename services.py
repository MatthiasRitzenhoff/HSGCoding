
#Declare globale dictionary
moviesDict = {}





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
    

#Fuction that adds the passed actor and movies to the dictionary
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


#Function that reads the file and stores the data in the dictionary
def readFile():
    #read the file
    f = open("movies.txt", "r")
    
    #Go through each line in the file and add the data to the dictionary
    for x in f:
        actor = getActor(x)
        movies = getMovies(x)
        addMoviesToDictionary(actor, movies)
        
    

#Function that is call when the user wants to have the actors that acted in specific movies
def handleOptionA(fstMovie, operator, sndMovie):
    
    #Get all actors that acted in each of the two movies
    actorsMovieOne = moviesDict[fstMovie]
    actorsMovieTwo = moviesDict[sndMovie]

    #Execute the logical operators
    if operator == "&":
        return (actorsMovieOne & actorsMovieTwo)
    elif operator == "|":
        return (actorsMovieOne | actorsMovieTwo)
    elif operator == "^":
        return (actorsMovieOne ^ actorsMovieTwo)
    else:
        print(operator + " is not a valid operator. Please use ],| or ^")
        return "Invalid Entry"


#Function that is called when the user wants have all actors that acted with the actor that was beeing passed
def handleOptionB(actor):
    #Define a set that will capture the output, thereby, all dublicates will be elminated automatically (property of a set)
    result = set()

    #Loop through every movie in the dictionary and capture all actors
    for movie in moviesDict.keys():
        #Store all actors for the correspoding movie in a variable
        curentActors = moviesDict[movie]

        #Check if the Actor that was passed by the user is in the list of all actors that acted in the current movie 
        if actor in curentActors:
            #Use the OR operator to combine the current result set and the set of all actors
            result = (result | curentActors)
    
    #Remove the actor that was passed by the user from the current set
    result.remove(actor)

    return result

#Function that returns all movies that are in the dictionary
def getAllMovies():
    cntr = 1
    returnStr = ""
    for x in moviesDict.keys():
        returnStr += x + ", "
        cntr+= 1
        if cntr%8 == 0:
            returnStr += "\n"
    
    return returnStr[:-2]

#Function that returns all Actors that are in the dictionary
def getAllActors():
    cntr = 1
    returnStr = ""
    
    helpSet = set()

    for x in list(moviesDict.values()):
        for y in x:
            helpSet.add(y)    
        
    
    for x in helpSet:
        returnStr += x + ", "
        cntr+= 1
        if cntr%8 == 0:
            returnStr += "\n"
    
    return returnStr[:-2]


#Call function to the file and story the data in a dictionary
readFile()
