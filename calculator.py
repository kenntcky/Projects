def button_click(num):
    global input_data

    input_data = input_data + str(num)
    input_label.set(input_data)

def equals():
    global input_data
    
    try:
        total = str(eval(input_data))
        input_label.set(total)
        input_data = total
    except ZeroDivisionError:
        input_label.set("Cannot divide by zero.")
        input_data = ""
    except SyntaxError:
        input_label.set("Double check your symbols.")
        input_data = ""

def backspace():
    global input_data

    input_data = input_data[:-1]
    input_label.set(input_data)

def clear():
    global input_data

    input_label.set("")
    input_data = ""


from tkinter import *

windows = Tk()
windows.geometry("500x600")
windows.title("Calculator")
windows.resizable(False,False)
windows.config(background="black")

input_data = ""
input_label = StringVar()

Label = Label(windows,textvariable=input_label,bg="white",fg="green",width=60,height=3,borderwidth=5,relief="raised",background="black",font=("consolas",20))
Label.pack()

frame = Frame(windows)
frame.pack()


divide = Button(frame,text="/",width=10,height=5,
                 command=lambda: button_click("/"))
divide.grid(row=0, column=0)

multiply = Button(frame,text="*",width=10,height=5,
                 command=lambda: button_click("*"))
multiply.grid(row=0, column=1)

backspaces = Button(frame,text="Del",width=24,height=5,
                 command=lambda: backspace())
backspaces.grid(row=0, column=2,columnspan=2)

button1 = Button(frame,text="1",width=10,height=5,
                 command=lambda: button_click(1))
button1.grid(row=1, column=0)

button2 = Button(frame,text="2",width=10,height=5,
                 command=lambda: button_click(2))
button2.grid(row=1, column=1)

button3 = Button(frame,text="3",width=10,height=5,
                 command=lambda: button_click(3))
button3.grid(row=1, column=2)

minus = Button(frame,text="-",width=10,height=5,
                 command=lambda: button_click("-"))
minus.grid(row=1, column=3)

button4 = Button(frame,text="4",width=10,height=5,
                 command=lambda: button_click(4))
button4.grid(row=2, column=0)

button5 = Button(frame,text="5",width=10,height=5,
                 command=lambda: button_click(5))
button5.grid(row=2, column=1)

button6 = Button(frame,text="6",width=10,height=5,
                 command=lambda: button_click(6))
button6.grid(row=2, column=2)

plus = Button(frame,text="+",width=10,height=5,
                 command=lambda: button_click("+"))
plus.grid(row=2, column=3)

button7 = Button(frame,text="7",width=10,height=5,
                 command=lambda: button_click(7))
button7.grid(row=3, column=0)

button8 = Button(frame,text="8",width=10,height=5,
                 command=lambda: button_click(8))
button8.grid(row=3, column=1)

button9 = Button(frame,text="9",width=10,height=5,
                 command=lambda: button_click(9))
button9.grid(row=3, column=2)

clears = Button(frame,text="C",width=10,height=5,
                 command=lambda: clear())
clears.grid(row=4, column=0)

button0 = Button(frame,text="0",width=10,height=5,
                 command=lambda: button_click(0))
button0.grid(row=4, column=1)

coma = Button(frame,text=".",width=10,height=5,
                 command=lambda: button_click("."))
coma.grid(row=4, column=2)

equal = Button(frame,text="=",width=10,height=11,
                 command=lambda: equals())
equal.grid(row=3, column=3,rowspan=2)

windows.mainloop()