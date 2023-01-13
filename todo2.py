import json
from datetime import date

#create a flag => check if todoDB.json is empty or not

emptyDoc = False #if doc is empty or not
task_count=0
task = {}

#use an infinite while loop => bcz until we tell the fn to stop it should run
while True:
    with open("todoDB.json", "r") as f:
        #we use with as to open files via open() fn which returns a file object
        #to make changes to json => a json package comes, using json.load() expects one parameter i.e a file object
    #with as => containing variables are global variable => so no problem of scope
    #inbuild fn in python => to check if file is empty or not => so only read operation required
    #or we could've done => f = open("todoDB", "r") => so from above => f is holding what open() is returning
    #todoData is a dictionary
        todoData = json.load(f) #load() expects an object holding the json file i.e f
        #here => todoData is an empty dictionary 
        # print(todoData)

    keys = list(todoData.keys()) #.keys() returns all the keys of the dictionary of type "dict-keys" => then typecast the keys into a list using list()
    currentDate = date.today()#is a datetime object => to store it in the dictionary => store it in from of a string 

    #check if todoData is blank or not => if yes => then new user => len() function returns the no of keys in the dictionary => so check if empty or not using len()
    #checking if the user is a new user or not
    if len(todoData) == 0:
        emptyDoc = True
        #so take input from the user
        username = input("\nHi there!! Welcome to TodoCLI, Please enter your name: ")
        todoData["name"] = username
        todoData["date"] = str(currentDate)
        print(f"Hey {username}! I hope you had a good start of teh day, let's plan your day together\n You can create your first task by typing create task or add task") #inside {} we can write any python code(inc loops also) and outside of {} the string exists => when we prefix a string with a "f" => then above is possible  
        cmd = input(">>") #use >> when we take input in cmd, input being create task or add task

        todoData["today"] = [] #when we mention tasks of today
        
        if cmd == "create task" or cmd == "add task":
            print("\nPlease provide details of your tasks as per the CLI instructions")
            print("\nAdd time in military format i.e if it's 9AM write 0900 or it's 9PM write 2100")

            #take the task decription as input
            task_description = input("\nPlease enter your task description: ")
            scheduled_time = input("\nPlease enter the scheduled time: ")

            #inside the list declare a dictionary then within that we need to insert the description and timing

            task = {
                "task_id" : task_count,
                "description" : task_description,
                "scheduled_time" : scheduled_time,
                "status":"TBD"
            }
            todoData["today"].append(task)

            with open("todoDB.json", "w") as f:#clears the todoDB.json file and load it to f with write mode
                json.dump(todoData, f, indent=4)#dumping smt to the json file => para => dictionary,file object, indentation
            # continue
            task_count=task_count+1
        elif cmd == "break" or cmd == "exit":
            break
#=> how do we know if a task is there or not => by the "today" list => check the size of today list or check if today list exists or not 
    elif "today" in list(todoData.keys()):
        #if there is a list of tasks of today => 1st load it and show it to the user which tasks are already there
        tasks = todoData["today"]
        username = todoData["name"]
        #each elem in tasks in a dictionary
        print(f"\nToday is {currentDate}")
        #show user all existing tasks
        print(f"Hey {username}, here are the tasks for your day")
        for task in tasks:
            print(f"\nTask {tasks.index(task) + 1}")
            print("\nTask decription: ", task["description"])
            print("\nScheduled time: ", task["scheduled_time"])
        
        print("\n add more tasks for the day")
        
        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your task decription: ")
            scheduled_time = input("\nEnter your scheduled time for the task: ")
            
            task = {
                "task_id":task_count,
                "description" : task_description,
                "scheduled_time" : scheduled_time,
                "status":"TBD"
            }

            todoData["today"].append(task)

            with open("todoDB.json", "r+") as f: #r+ => to append data to what's in the file
                f.seek(0)   #f.seek(0) => it will point to the beginning of the file
                #f.seek(2) => it will point to the end of the file
                json.dump(todoData, f, indent = 4)
            task_count=task_count+1

            print("\nTask created successsfully")
            print("\ntype <create task> or <add task> to add more tasks")
            print("\ntype <done> or <exit> to exit from the app")
            continue

        elif cmd == "done" or cmd == "exit":
                break
        elif cmd=="delete user":
            todoData={}
            with open("todoDB.json","w") as f:
                f.seek(0)
                json.dump(todoData,f,indent=4)
        # elif cmd=="delete all task":
        #     todoData["Today"]=[]
        #     with open("todoDB.json","w") as f:
        #         json.dump(todoData,f,indent=4)
        elif cmd=="mark task as done":
            tasks=todoData["today"]
            username=todoData["name"]
            print(f"\nToday is {currentDate}")
            #show the user all existing tasks
            print(f"\nHey {username} ,here are the task for your day")
            for task in tasks:
                print(f"\n Task{tasks.index(task)+1}")
                print("\nTask decription: ", task["description"])
                print("\nScheduled time: ", task["scheduled_time"])
                print("\nStatus:",task["status"])
            #status_cmd=input("\ntask>> ")
            task_id=int(input("\nEnter task id:"))
            for task in tasks:
                if task["task_id"]==task_id:
                    todoData["today"][tasks.index(task)]["status"]="DONE"
                else:
                    continue
            with open("todoDB.json","r+") as f:
                json.dump(todoData,f,indent=4)  
            continue  
