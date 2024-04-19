import tkinter
import random
colors = ["red","blue","green","black","orange","white","purple"]
score = 0
timeleft = 30
def startGame(event):
    if timeleft == 30:
        countdown()
    nextColor()
def nextColor():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1
        e.delete(0,tkinter.END)
        random.shuffle(colors)
        label1.config(fg = str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text = "Score: "+ str(score))
def countdown():
    global timeleft
    if timeleft>0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft))
        timeLabel.after(1000,countdown)
window = tkinter.Tk()
window.title("Tech Club Color Game")
window.geometry("375x200")
inst = tkinter.Label(window,text ="Type in the color of the words, and not the word text!",font=('Calibri',12))
inst.pack()
scoreLabel = tkinter.Label(window,text="Press enter to start",font=("Calibri",12))
scoreLabel.pack()
timeLabel = tkinter.Label(window,text ="Time left: " +str(timeleft),font=("Calibri",12))
timeLabel.pack()
label1 = tkinter.Label(window,font=("Helvetica",60))
label1.pack()
e = tkinter.Entry(window)
window.bind('<Return>',startGame)
e.pack()
e.focus_set()
window.mainloop()
