from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import names

# BACKEND

def search():
    Gender=gender.get()  
    Type= types.get()
    text.delete(0.0,END)

    if Type=='Full Name':
        name=names.get_full_name(gender=Gender)
        text.insert('end',name)

    elif Type=="First Name":
        name=names.get_first_name(gender=Gender)
        text.insert('end',name)

    elif Type=="Last Name":
        name=names.get_last_name()
        text.insert('end',name)


root=Tk()

#Layout and title
root.geometry("700x300")
root.title("Name Generator")

#Heading
l= Label(root, text="Name Generator", font=('verdana',15,'bold'),bg='indigo',fg='white')
l.place(x=250,y=10)

#Gender Heading
l1 = Label(root,text="Gender",font=('verdana',10,'bold'))
l1.place(x=80,y=70)

g= tk.StringVar()
gender=ttk.Combobox(root,width=13, textvariable=g, state="readonly", font=('verdana',10,'bold'))
gender['values']=('Male','Female')
gender.place(x=80,y=100)
gender.current(0)

# Name Type
l2 = Label(root,text="Type",font=('verdana',10,'bold'))
l2.place(x=320, y=70)

t = tk.StringVar()
types = ttk.Combobox(root,width = 13, textvariable=t, state="readonly",font=('verdana',10,'bold'))
types['values']=('Full Name','First Name','Last Name')
types.place(x=320,y=100)
types.current(0)

#Display screen
text = ScrolledText(root, width=45, height=4)
text['font']=('verdana',10,'bold')
text.place(x=130, y=180)

#Search Button
button=Button(root,text="Search",font=('verdana',10,'bold'),command=search)
button.place(x=540,y=95)


root.mainloop()