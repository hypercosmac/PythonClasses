from tkinter import *
from tkinter import messagebox
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0,"end")
        task_list.append(task)
    else:
        messagebox.showwarning("Error","Please enter a task")
def deleteTask():
    lb.delete(ANCHOR)
def save():
    tasks = open("tasks.txt","w")
    for t in task_list:
        tasks.write(t+",")
    tasks.close()

screen = Tk()
screen.title('Python To-Do List')
frame = Frame(screen)
frame.pack(pady=10)

lb = Listbox(frame, width = 25, height = 8, font=('Calibri',16))
lb.pack(side=LEFT, fill=BOTH)

initfile = open("tasks.txt","r")

inittasks = initfile.read()
task_list = list(inittasks.split(","))

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

label = Label(screen,text="Type your task below and click on Add task")
label.pack()
my_entry = Entry(screen,font=('Calibri',20))
my_entry.pack(pady=20)

btn_frame = Frame(screen)
btn_frame.pack(pady=20)
addTask = Button(btn_frame,text="Add Task",font=('Calibri',14),
                 padx=20,pady=10,command=newTask)
addTask.pack(fill=BOTH,expand=True, side=LEFT)
delTask = Button(btn_frame,text="Task Done", font=('Calibri',14,),
                 padx=20,pady=10,command=deleteTask)
delTask.pack(fill=BOTH, expand=True, side=LEFT)
saveBtn = Button(btn_frame,text="Save Tasks", font=('Calibri',14,),
                 padx=20,pady=10,command=save)
saveBtn.pack()
screen.mainloop()
