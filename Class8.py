import tkinter

window = tkinter.Tk()
window.title("Hello World")

def signin():
    tkinter.Label(window, text = "You are being signed in!").grid(row=4)
    file.write(user.get())
    file.write("\n"+str(password.get()))
    file.close()
file = open("Userinfo.txt","w")
'''
label = tkinter.Label(window,text = "Welcome to my first TKinter program").pack()
button = tkinter.Button(window,text = "Click on me!")
button.pack()
btn1 = tkinter.Button(window,text="Red",fg="red",bg="black").pack()
chk1 = tkinter.Checkbutton(window, text = "green", fg="green").pack()
chk2 = tkinter.Checkbutton(window, text = "blue",fg="blue").pack()
'''
tkinter.Label(window, text="Username").grid(row = 0)
user = tkinter.Entry(window)
user.grid(row = 0, column = 1)
tkinter.Label(window, text="Password").grid(row = 1)
password = tkinter.Entry(window, show="*")
password.grid(row=1,column=1)
tkinter.Checkbutton(window, text = "Keep me logged in").grid(columnspan = 2)
tkinter.Button(window,text = "Sign in", command=signin).grid(columnspan = 2)

window.mainloop()
