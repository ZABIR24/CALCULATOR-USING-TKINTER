from tkinter import *
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    GUI = Tk()
    GUI.configure(background="white")
    GUI.title("Simple Calculator")
    GUI.geometry("810x450")
    
    equation = StringVar()
    expression_field = Entry(GUI,textvariable=equation)
    expression_field.grid(columnspan=500,ipadx=100)
    
    button1=Button(GUI,text="1",fg="black",bg="white",command=lambda:press(1),height=3,width=21)
    button1.grid(row=2,column=0)
    
    button2=Button(GUI,text="2",fg="black",bg="white",command=lambda:press(2),height=3,width=21)
    button2.grid(row=2,column=1)
    
    button3=Button(GUI,text="3",fg="black",bg="white",command=lambda:press(3),height=3,width=21)
    button3.grid(row=2,column=2)
    
    button4=Button(GUI,text="4",fg="black",bg="white",command=lambda:press(4),height=3,width=21)
    button4.grid(row=3,column=0)
    
    button5=Button(GUI,text="5",fg="black",bg="white",command=lambda:press(5),height=3,width=21)
    button5.grid(row=3,column=1)
    
    button6=Button(GUI,text="6",fg="black",bg="white",command=lambda:press(6),height=3,width=21)
    button6.grid(row=3,column=2)
    
    button7=Button(GUI,text="7",fg="black",bg="white",command=lambda:press(7),height=3,width=21)
    button7.grid(row=4,column=0)
    
    button8=Button(GUI,text="8",fg="black",bg="white",command=lambda:press(8),height=3,width=21)
    button8.grid(row=4,column=1)
    
    button9=Button(GUI,text="9",fg="black",bg="white",command=lambda:press(9),height=3,width=21)
    button9.grid(row=4,column=2)
    
    button0=Button(GUI,text="0",fg="black",bg="white",command=lambda:press(0),height=3,width=21)
    button0.grid(row=5,column=0)
    
    plus_button=Button(GUI,text="+",fg="black",bg="white",command=lambda:press("+"),height=3,width=21)
    plus_button.grid(row=2,column=3)
    
    minus_button=Button(GUI,text="-",fg="black",bg="white",command=lambda:press("-"),height=3,width=21)
    minus_button.grid(row=3,column=3)
    
    multiply_button=Button(GUI,text="*",fg="black",bg="white",command=lambda:press("*"),height=3,width=21)
    multiply_button.grid(row=4,column=3)
    
    divide_button=Button(GUI,text="/",fg="black",bg="white",command=lambda:press("/"),height=3,width=21)
    divide_button.grid(row=5,column=3)
    
    equal_button=Button(GUI,text="=",fg="black",bg="white",command=equalpress,height=3,width=21)
    equal_button.grid(row=5,column=2)
    
    clear_button=Button(GUI,text="clear",fg="black",bg="white",command=clear,height=3,width=21)
    clear_button.grid(row=5,column='1')
    
    point_button=Button(GUI,text=".",fg="black",bg="white",command=lambda:press("."),height=3,width=21)
    point_button.grid(row=6,column=0)
    
    GUI.mainloop()