#https://www.youtube.com/watch?v=S3AaSwpb5GE
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Learn To Code at Codemy.com')

#showinfo, showwarning, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion("This is my Popup!", "Hello World!")
    Label(root, text = response).pack
    if response == 1:
        Label(root, text="You Clicked Yes").pack
    else:
        Label(root, text="You Clicked No").pack

Button(root, text="Popup", command=popup).pack()

mainloop()