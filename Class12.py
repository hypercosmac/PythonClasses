import tkinter as tk
window = tk.Tk()
window.title = ("Password Manager")

def saveCred():
    encrypted_pass = ""
    orig_pass = password_field.get()
    for i in orig_pass:
        nc = ord(i)+1
        encrypted_pass = encrypted_pass+chr(nc)
        print(encrypted_pass)
    cred = open("creds.txt","w")
    cred.write("\n"+username_field.get()+" "+encrypted_pass)
    cred.close()
def loadCred():
    cred = open("creds.txt","r")
    ret = cred.read()
    for i in range(len(ret)):
        username = ""
        password = ""
        if ord(ret[i]) != 32:
            username = username+ret[i]
        else:
            i+=1
            for n in range (i,len(ret)):
                password = password+ret[n-1]
    print(username+" "+password)

instructions = tk.Label(window,text="Enter your username and password and press enter to save")
label1 = tk.Label(window,text="Username: ")
label1.grid(row=1,column=0)
username_field = tk.Entry(window)
username_field.grid(row=1,column=1)

label2 = tk.Label(window,text="Password: ")
label2.grid(row=2,column=0)
password_field = tk.Entry(window)
password_field.grid(row=2,column=1)

button_save = tk.Button(window,text="Save",command=saveCred).grid(row=3,column=1)
button_load = tk.Button(window,text="Load Passwords", command=loadCred).grid(row=4,column=1)
