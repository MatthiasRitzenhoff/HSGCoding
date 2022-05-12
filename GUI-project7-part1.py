#Import the required libraries
import tkinter as tk

#Asking four questions after another
questions = ['Do you want to get different intersections of actors depending on two movies? Answer with Movies. If you prefer to have the co-actors of an actor displayed, answer with Actors.']
#Everytime the answers are either Yes or No
answers = ['Movies', 'Actors']

root = tk.Tk()
root.minsize(300, 300)

def ask():
    if questions:
        lab_text.set(questions.pop(0))

for index, answer in enumerate(answers):
    lab_text = tk.StringVar()
    lab = tk.Label(root, textvariable=lab_text)
    lab.grid(row=0, column=0)
    b = tk.Button(root, text=answer, command=ask)
    b.grid(row=1, column=index)

#Initialize label
ask()

root.mainloop()