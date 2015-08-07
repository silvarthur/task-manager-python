import pickle
from task import Task

l = []

while True:

    print "1 - Create a task"
    print "2 - Delete a task"
    print "3 - Show all tasks"
    print "4 - Exit"

    option = input("What do you want to do? ")

    if(option == 1):
        name = raw_input("What's the task: ")
        start_date = raw_input("Start date: ")
        end_date = raw_input("End date: ")
        description = raw_input("Description: ")

        with open("tasks.obj","ab") as f:
            x = Task(name, start_date, end_date, description)
            pickle.dump(x,f)

    elif(option == 2):
        print "2"
    elif(option == 3):
        with open("tasks.obj","rb") as v:

            while True:
                try:
                    print pickle.load(v)
                except EOFError:
                    break
    elif(option == 4):
        break