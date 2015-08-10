import pickle
import ttk
from Tkinter import *
from task import Task

def create_list_tasks(filename):
    l = []
    with open(filename,"rb") as f:
        while True:
            try:
                l.append(pickle.load(f))
            except EOFError:
                break
    return l

def new_task_window():
    def create_task():
        with open("tasks.obj","ab") as f:
            name = name_entry.get()
            start_date = status_entry.get()
            end_date = priority_entry.get()
            description = due_date_entry.get()
            task = Task(name,start_date,end_date,description)
            pickle.dump(task,f)
        show_all_tasks(table)
        top.destroy()

    def clear():
        name_entry.delete(0,END)
        status_entry.delete(0,END)
        priority_entry.delete(0,END)
        due_date_entry.delete(0,END)

    def cancel():
        top.destroy()

    top = Toplevel()
    top.title("New Task")
    top.resizable(width=FALSE,height=FALSE)

    name_label = Label(top,text="Name: ")
    status_label = Label(top,text="Status: ")
    priority_label = Label(top,text="Priority: ")
    due_date_label = Label(top,text="Due date: ")

    name_entry = Entry(top)
    status_entry = Entry(top)
    priority_entry = Entry(top)
    due_date_entry = Entry(top)

    create_button = Button(top,text="Create Task",width=10,command=create_task)
    clear_button = Button(top,text="Clear",width=10,command=clear)
    cancel_button = Button(top,text="Cancel",width=10,command=cancel)

    name_label.grid(row=0,column=0,sticky=W)
    status_label.grid(row=1,column=0,sticky=W)
    priority_label.grid(row=2,column=0,sticky=W)
    due_date_label.grid(row=3,column=0,sticky=W)

    name_entry.grid(row=0,column=1,columnspan=2,sticky=W+E+N+S)
    status_entry.grid(row=1,column=1,columnspan=2,sticky=W+E+N+S)
    priority_entry.grid(row=2,column=1,columnspan=2,sticky=W+E+N+S)
    due_date_entry.grid(row=3,column=1,columnspan=2,sticky=W+E+N+S)

    create_button.grid(row=8,column=0)
    clear_button.grid(row=8,column=1)
    cancel_button.grid(row=8,column=2)

def show_all_tasks(table):
    counter = 1
    tasks = create_list_tasks("tasks.obj")
    table.delete(*table.get_children())
    for task in tasks:
        name = task.name
        status = task.status
        priority = task.priority
        due_date = task.due_date
        table.insert("",counter,text="Task "+str(counter),
                     values=(name,status,priority,due_date))
        #table.insert("", 3, "dir3", text="Dir 3")
        #table.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))
        counter += 1

def delete_task():
    print "test"
    task = table.focus()
    for child in table.get_children():
        if task == child:
            table.delete(child)
    #tasks = create_list_tasks(filename)
    #with open(filename,"wb") as f:
        #for index in tasks:
            #if index.name != task:
                #pickle.dump(index,f)

def exit():
    root.destroy()

root = Tk()
root.wm_title("Task Manager")
root.resizable(width=FALSE,height=FALSE)

table = ttk.Treeview(root)
table["columns"]=("one","two","three","four")
table["height"]="10"
table.heading("one", text="Name")
table.heading("two", text="Status")
table.heading("three", text="Priority")
table.heading("four", text="Due date")

show_all_tasks(table)

new_task_button = Button(root,text="Create Task",width=10,command=new_task_window)
delete_task_button = Button(root,text="Delete Task",width=10,command=delete_task)
exit_button = Button(root,text="Exit",width=10,command=exit)

table.grid(row=0,columnspan=3)

new_task_button.grid(row=1)
delete_task_button.grid(row=1,column=1)
exit_button.grid(row=1,column=2)

root.mainloop()