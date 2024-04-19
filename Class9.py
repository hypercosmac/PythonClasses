from tkinter import *
window = Tk()
window.title("Calculator")
def btn_click(item):
    global expression
    expression = expression+str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
expression = ""
input_text = StringVar()
input_field = Entry(window, font=('arial',18,'bold'),textvariable = input_text, justify = RIGHT).grid(row=0,column=1,columnspan=3)
#btns_frame = Frame(window,width=312,heigh=272.5,bg="grey").grid()
clear = Button(window,text="C",width=32,height=3,command = lambda: btn_clear()).grid(row=1,columnspan=3)
divide = Button(window, text="/",fg="#ff0000",width=10,height=3, command = lambda:btn_click("/")).grid(row = 1,column=3)
seven = Button(window,text="7", width=10,height=3,command = lambda:btn_click(7)).grid(row=2,column=0)
eight = Button(window,text="8", width=10,height=3,command = lambda:btn_click(8)).grid(row=2,column=1)
nine = Button(window,text="9", width=10, height=3,command = lambda:btn_click(9)).grid(row=2,column=2)
multiply = Button(window,text="*", width=10, height=3,command = lambda:btn_click("*")).grid(row=2,column=3)
four = Button(window,text="4",width=10,height=3, command = lambda:btn_click(4)).grid(row=3,column=0)
five = Button(window,text="5",width=10,height=3, command = lambda:btn_click(5)).grid(row=3,column=1)
six = Button(window,text="6",width=10,height=3, command = lambda:btn_click(6)).grid(row=3,column=2)
minus = Button(window,text="-",width=10,height=3, command = lambda:btn_click("-")).grid(row=3,column=3)
one = Button(window,text="1",width=10,height=3, command = lambda:btn_click(1)).grid(row=4,column=0)
two = Button(window,text="2",width=10,height=3, command = lambda:btn_click(2)).grid(row=4,column=1)
three = Button(window,text="3",width=10,height=3, command = lambda:btn_click(3)).grid(row=4,column=2)
plus = Button(window,text="+",width=10,height=3, command = lambda:btn_click("+")).grid(row=4,column=3)
zero = Button(window,text="0",width=22,height=3, command = lambda:btn_click(0)).grid(row=5,column=0,columnspan=2)
point = Button(window,text=".",width = 10,height=3, command = lambda:btn_click(".")).grid(row=5,column=2)
equal = Button(window,text="=",width = 10,height=3, command = lambda:btn_equal()).grid(row=5,column=3)
window.mainloop()
