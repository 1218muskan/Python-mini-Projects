from tkinter import *
from random import *

num="1234567890"
alphanum="abcdefghijklmonpqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum="abcdefghijklmonpqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){}"

def Create_Pass():
    User_Choice = Tchoice.get()

    if User_Choice=="":
        resultBox.delete(0.0,END)
        resultBox.insert(END,"\n Select the type of password you'd like to generate")

    length = int(pass_length.get())
    randPass=[]
    for i in range(length):
        randPass.append(choice(User_Choice))


    result="".join(randPass)
    display_result = "\n Yor Password is: "+result
    resultBox.delete(0.0,END)
    resultBox.insert(END,display_result)


# Tkinter window
window = Tk()
window.title("Random Password Generator")
window.geometry("800x500")

window.minsize(800,500)
window.maxsize(800,500)

progName = Label(window, font=('Stencil',18), text="Password Generator", fg="indigo")
progName.grid(row=1,column=3, padx=200,pady=30)

chooseType = Label(window,font=('Times New Roman',15,'bold'),text="Choose a type among 3")
chooseType.place(relx=.03, rely=.25)

Tchoice= StringVar()
Numchoice = Radiobutton(window, font=('corbel',10,'italic'),text="Numeric", variable=Tchoice, value=num)
Numchoice.place(relx=.3,rely=.35)
AlphaNumchoice=Radiobutton(window,font=('corbel',10,'italic'),text="AlphaNumeric",variable=Tchoice,value=alphanum)
AlphaNumchoice.place(relx=.3,rely=.4)
Salphachoice=Radiobutton(window,font=('corbel',10,'italic'),text="Special",variable=Tchoice,value=spalphanum)
Salphachoice.place(relx=.3,rely=.45)

size = Label(window, text='Size', font=('copperplate Gothic',10,'bold'))
size.place(relx=.65,rely=.4)

pass_length = Spinbox(window, from_=8, to=100)
pass_length.place(relx=.73, rely=.4)
pass_length.config(state='readonly')

GenButton = Button(window,text="Generate",command=Create_Pass)
GenButton.place(relx=.45, rely=.57)

resultBox = Text(window,height=6, width=70)
resultBox.place(relx=.14, rely=.7)

window.mainloop()