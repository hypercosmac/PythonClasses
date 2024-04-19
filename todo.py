from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter a task.")

def deleteTask():
    lb.delete(ANCHOR)
    
screen = Tk()
screen.title('Python To-Do List')

frame = Frame(screen)
frame.pack(pady=10)

lb = Listbox(frame,width=25,height=8)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(screen,font=('times', 24))
my_entry.pack(pady=20)

button_frame = Frame(screen)
button_frame.pack(pady=20)

addTask_btn = Button(button_frame,text='Add Task',font=('times 14'),padx=20,pady=10,command=newTask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame,text='Delete Task',font=('times 14'),padx=20,pady=10,command=deleteTask)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

screen.mainloop()
