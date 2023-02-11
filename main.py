from tkinter import *



hfgygyjy
home=Tk()
home.title("Калькулятор")
home.geometry("600x600")
home.resizable(width=False,height=False)

def add_digit(digit):
    calc.insert(END,digit)

def dele():
    calc.delete(0,END)

def count_result():
    text=calc.get()
    result=0

    if "+"in text:
        splitted_text=text.split("+")
        first=float(splitted_text[0])
        second=float(splitted_text[1])
        result=first+second
        print(result)
    if "-" in text:
        splitted_text = text.split("-")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first - second
        print(result)
    if "*" in text:
        splitted_text = text.split("*")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first * second
        print(result)
    if "/" in text:
        splitted_text = text.split("/")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first / second
        print(result)

calc=Entry(home)
calc.grid(row=0,column=0,columnspan=3)

button1=Button(text="7",bg="white",fg="black",width=10,command=lambda :add_digit(7))
button2=Button(text="4",bg="white",fg="black",width=10,command=lambda :add_digit(4))
button3=Button(text="1",bg="white",fg="black",width=10,command=lambda :add_digit(1))
button4=Button(text="=",bg="white",fg="black",width=10,command=count_result)
button5=Button(text="8",bg="white",fg="black",width=10,command=lambda :add_digit(8))
button6=Button(text="5",bg="white",fg="black",width=10,command=lambda :add_digit(5))
button7=Button(text="2",bg="white",fg="black",width=10,command=lambda :add_digit(2))
button8=Button(text=".",bg="white",fg="black",width=10,command=lambda :add_digit("."))
button9=Button(text="9",bg="white",fg="black",width=10,command=lambda :add_digit(9))
button10=Button(text="6",bg="white",fg="black",width=10,command=lambda :add_digit(6))
button11=Button(text="3",bg="white",fg="black",width=10,command=lambda :add_digit(3))
button12=Button(text="C",bg="white",fg="black",width=10,command=dele)
button13=Button(text="+",bg="white",fg="black",width=10,command=lambda : add_digit("+"))
button14=Button(text="-",bg="white",fg="black",width=10,command=lambda : add_digit("-"))
button15=Button(text="*",bg="white",fg="black",width=10,command=lambda : add_digit("*"))
button16=Button(text="/",bg="white",fg="black",width=10,command=lambda : add_digit("/"))
button17=Button(text="0",bg="white",fg="black",width=10,command=lambda : add_digit(0))


button1.grid(row=1,column=0)
button2.grid(row=2,column=0)
button3.grid(row=3,column=0)
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=1,column=1)
button7.grid(row=2,column=1)
button8.grid(row=3,column=1)
button9.grid(row=4,column=2)
button10.grid(row=1,column=2)
button11.grid(row=2,column=2)
button12.grid(row=3,column=2)
button13.grid(row=5,column=0,columnspan=2,stick='we')
button14.grid(row=2,column=3)
button15.grid(row=3,column=3)
button16.grid(row=4,column=3)
button17.grid(row=1,column=3)


mainloop()



