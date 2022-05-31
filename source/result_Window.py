#Import the required Libraries
from tkinter import *





def startMoviesResultWindow(msg, result):

    #Main
    window = Tk()
    window.title("Who's Who in Hollywood (Project 7)")
    window.configure(background="White")
    window.geometry("400x100")

    def formatResult(resultMSg, rawString):
        rsltString = ""
        for x in rawString:
            rsltString += x + "\n"
        
        print("reslt strin is: " + rsltString)
        if rsltString == "":
            rsltString = " Sorry, there is no result for your input."
        else:
            rsltString = resultMSg + rsltString
        return rsltString

    #Create label
    Label(window, text=formatResult(msg, result), bg="white", fg="black", font="non 10").grid(row=1, column=0)

    

    window.mainloop()