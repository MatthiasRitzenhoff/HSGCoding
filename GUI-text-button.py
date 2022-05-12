import tkinter as tk

#Set the geometry of the Tkinter frame
win.geometry("750x250")

#Asking four questions after another
questions = ['Question 1', 'Question 2',
             'Question 3', 'Question 4', 'Question 5']
#Everytime the answers are either Yes or No
answers = ['Yes', 'No']

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