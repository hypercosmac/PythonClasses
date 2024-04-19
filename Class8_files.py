import tkinter

window = tkinter.Tk()
window.title("Hello World")

def signin():
    tkinter.Label(window, text = "You are being signed in!").grid(row=4)


label = tkinter.Label(window,text = "Welcome to my first TKinter program").pack()
button = tkinter.Button(window,text = "Click on me!")
button.pack()
btn1 = tkinter.Button(window,text="Red",fg="red",bg="black").pack()
chk1 = tkinter.Checkbutton(window, text = "green", fg="green").pack()
chk2 = tkinter.Checkbutton(window, text = "blue",fg="blue").pack()
tkinter.Label(window, text="Username").grid(row = 0)
tkinter.Entry(window).grid(row = 0, column = 1)
tkinter.Label(window, text="Password").grid(row = 1)
tkinter.Entry(window, show="*").grid(row=1,column=1)
tkinter.Checkbutton(window, text = "Keep me logged in").grid(columnspan = 2)
tkinter.Button(window,text = "Sign in", command=signin).grid(columnspan = 2)
'''
def leftclick(event):
    tkinter.Label(window, text = "Left click",width = "30").pack()
def middleclick(event):
    tkinter.Label(window, text = "Middle click",width = "30").pack()
def rightclick(event):
    tkinter.Label(window, text = "Right click",width = "30").pack()

window.bind("<Button-1>",leftclick)
window.bind("<Button-3>",middleclick)
window.bind("<Button-2>",rightclick)

icon = tkinter.PhotoImage(file = "growth.png")
tkinter.Label(window,image = icon).pack()
'''
window.mainloop()
