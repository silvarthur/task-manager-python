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

        x = Task(name, start_date, end_date, description)
        l.append(x)

    elif(option == 2):
        print "2"
    elif(option == 3):
        print "3"
    elif(option == 4):
        break