class Task:

    def __init__(self,name,status,priority,due_date):
        print "You've just created a task! Now, do it!" + "\n"
        self.name = name
        self.status = status
        self.priority = priority
        self.due_date = due_date