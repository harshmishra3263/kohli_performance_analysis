import json
from datetime import date 

emptyDoc=False

# f= open("todoDB.json","r")
task={}
while True:
    with open("todoDB.json","r") as f:
        #reading the todoDB.json
        todoData=json.load(f)
    #print(todoData)

#print(todoData)
    keys=list(todoData.keys())
    currentDate=date.today()
   
    #checking whether the user is the new user or not
    if len(todoData)==0:
        emptyDoc=True
        username=input("\nHi there!! welcome to todocli ,please enter your name")
        todoData["name"]=username
        todoData["date"]=str(currentDate)
        print(f"Hey {username}! I hope you had a good start of the day,lets plan your day together .You can create your first taks by typing create task or add task")

        cmd=input(">>")

        todoData["today"]=[]
        if cmd == "create task" or cmd=="add task":
            print("\nPlease provide about your tasks as per the cli instructions\n")
            print("\n Add time in milatiary format\n")

            #tasks discriptions as input
            task_discription =input("\nPlease enter your tasks discription:  \n")
            scheduled_time= input("\nplease enter the schedule time:   \n ")
            task={
                "discription":task_discription,
                "scheduled_time":scheduled_time
            }
            todoData["today"].append(task)
            with open("todoDB.json","w") as f:
                json.dump(todoData,f,indent=4)
               # continue
        elif cmd == "break" or cmd=="exit":
            break
    elif "today" in list(todoData.keys()):
        tasks=todoData["today"]
        username=todoData["name"]

        print(f"Today is {currentDate}")
        #show the user all existing tasks
        print(f"\n Hey,{username},here are the tasks for your day")
        for task in tasks:
            print(f"\nTask{tasks.index(task)+1}") 
            print("\nTask discription:",task["discription"])
            print("\nScheduled time:",task["scheduled_time"])

        print("\nadd more tasks for the day")
        cmd=input(">>")
        if cmd== "create task" or cmd=="add task":
            task_discription= input("\nEnter your tasks discription:")
            scheduled_time=input("\nEnter the scheduled time")
            task={
                "description": task_discription,
                "Scheduled_time": scheduled_time
            }
            todoData["today"].append(task)
            with open("todoDB.json","r+") as f:
                f.seek(0)
                json.dump(todoData,f,indent=4)
            print("\ntasks created successfully")
            print("\n Type <create task> or <add task> to add more tasks")
            print("\n Type <done> or <exit> from the app")
            continue
        elif cmd=="done" or cmd=="exit":
            break
        elif cmd=="delete user":
            blank_dictionary={}
            with open("todoDB.json","w") as f:
                json.dump(blank_dictionary,f,indent=4)
       



