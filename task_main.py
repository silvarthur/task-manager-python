import pickle
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

def create_task(filename,name,end_date,start_date,description):
    with open(filename,"ab") as f:
        task = Task(name,start_date,end_date,description)
        pickle.dump(task,f)

def delete_task(filename,task):
    tasks = create_list_tasks(filename)
    with open(filename,"wb") as f:
        for index in tasks:
            if index.name != task:
                pickle.dump(index,f)

l = []

while True:

    print "1 - Create a task"
    print "2 - Delete a task"
    print "3 - Show all tasks"
    print "4 - Exit" + "\n"

    option = input("What do you want to do? ")

    if(option == 1):
        name = raw_input("\n" + "What's the task: ")
        start_date = raw_input("Start date: ")
        end_date = raw_input("End date: ")
        description = raw_input("Description: ")
        create_task("tasks.obj",name,start_date,end_date,description)
        #with open("tasks.obj","ab") as f:
            #x = Task(name, start_date, end_date, description)
            #pickle.dump(x,f)
    elif(option == 2):
        task = raw_input("\n" + "What task do you want to delete: ")
        delete_task("tasks.obj",task)
        #inp = raw_input("What task do you want to delete?")
        #tasks = create_list_tasks("tasks.obj")
        #with open("tasks.obj","wb") as f:
            #for task in tasks:
                #if task.name != inp:
                    #pickle.dump(task,f)
    elif(option == 3):
        l = create_list_tasks("tasks.obj")
        for task in l:
            print "\n" + "Task: " + task.name
            print "Start date: " + task.start
            print "End date: " + task.end
            print "Description: " + task.description + "\n"
    elif(option == 4):
        break