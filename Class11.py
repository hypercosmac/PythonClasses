import tkinter as tk
import random

window = tk.Tk()
window.title = ("Rock Paper Scissors Game")

U_score = 0
C_score = 0
U_choice = ""
C_choice = ""

def rock():
    global U_choice
    global C_choice
    U_choice = 'rock'
    C_choice = random.choice(['rock','paper','scissor'])
    result(U_choice,C_choice)
def paper():
    global U_choice
    global C_choice
    U_choice = 'paper'
    C_choice = random.choice(['rock','paper','scissor'])
    result(U_choice,C_choice)
def scissor():
    global U_choice
    global C_choice
    U_choice = 'scissor'
    C_choice = random.choice(['rock','paper','scissor'])
    result(U_choice,C_choice)
def conv_choice(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def conv_num(num):
    rps = {0:'rock',1:'paper',2:'scissor'}
    return rps[num]
def result(human_choice,comp_choice):
    global U_score
    global C_score
    user=conv_choice(human_choice)
    comp=conv_choice(comp_choice)
    print("Computer chose: ",comp_choice)
    if (user == comp):
        print("Tie")
    elif ((user-comp)%3==1):
        print("You win")
        U_score+=1
    else:
        print("Computer wins")
        C_score+=1
    text_a = tk.Text(window,height=12,width=30)
    text_a.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice: {cc} \nYour Score: {u} \nComputer Score: {c}".format(uc=U_choice,cc=C_choice,u=U_score,c=C_score)
    text_a.insert(tk.END,answer)
button1 = tk.Button(text="    🪨Rock   ",fg="skyblue",font=("Calibri",30),command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="    📄Paper   ",fg="red",font=("Calibri",30),command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="  ✂️Scissor  ",fg="lightgreen",font=("Calibri",30),command=scissor)
button3.grid(column=0,row=3)
window.mainloop()
