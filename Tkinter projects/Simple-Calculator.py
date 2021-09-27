from tkinter import *
expression=""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# For caluculation
def equalpress():
    try:
        global expression
        total= str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression= " "

def clear():
    expression= " "
    equation.set(expression)


root=Tk()

root.geometry("400x470")
# set minimum window size value
root.minsize(400, 470)
 
# set maximum window size value
root.maxsize(400, 470)

root.title("Simple Calculator")
root.configure(bg="lightblue")

heading = Label(root, text="Calculator", font=('verdana',15,'bold'), bg="lightpink")
heading.place(x=140,y=15)

equation = StringVar()
txt = Entry(root,state='readonly', font=('times new roman',25,'bold'), textvariable=equation)
txt.grid(row=6,column=3, pady=60, padx=30, sticky='W')

txt_frame =Frame(txt, bd=10,bg="crimson")
txt_frame.place(x=2,y=2,width=450)


#Button Fixing
seven = Button(text="7", width=9,height=3, command= lambda:press(7))
seven.place(x=30,y=130)

eight = Button(text="8", width=9,height=3, command= lambda:press(8))
eight.place(x=120,y=130)

nine = Button(text="9", width=9,height=3, command= lambda:press(9))
nine.place(x=210,y=130)

ce = Button(text="CE", width=9,height=3, command= lambda:clear())
ce.place(x=300,y=130)

four = Button(text="4", width=9,height=3, command= lambda:press(4))
four.place(x=30,y=210)

five = Button(text="5", width=9,height=3, command= lambda:press(5))
five.place(x=120,y=210)

six = Button(text="6", width=9,height=3, command= lambda:press(6))
six.place(x=210,y=210)

zero = Button(text="0", width=9,height=3, command= lambda:press(0))
zero.place(x=300,y=210)

one = Button(text="1", width=9,height=3, command= lambda:press(1))
one.place(x=30,y=290)

two = Button(text="2", width=9,height=3, command= lambda:press(2))
two.place(x=120,y=290)

three = Button(text="3", width=9,height=3, command= lambda:press(3))
three.place(x=210,y=290)

plus = Button(text="+", width=10,height=3, command= lambda:press('+'))
plus.place(x=300,y=290)

divide = Button(text="/", width=9,height=3, command= lambda:press('/'))
divide.place(x=30,y=370)

multiply = Button(text="X", width=9,height=3, command= lambda:press('*'))
multiply.place(x=120,y=370)

sub = Button(text="-", width=9,height=3, command= lambda:press('-'))
sub.place(x=210,y=370)

equal = Button(text="=", width=10,height=3, command= lambda:equalpress())
equal.place(x=300,y=370)

root.mainloop()