def addtask(tasks):
    desc=input("enter description of task  ")
    tasks.append({"description":desc ,"comp":False})
    print("the task is added")
    print("\n")


def viewtask(tasks):
   
    if not tasks:
        print("no tasks")
        print("\n")
    else :
        for i, task in enumerate(tasks)  :
            stat="incompleted"
            if task["comp"]:
                stat="completed"
            print(f"task {i} : {task['description']}-{stat}")
        print("\n")

def markcomp(tasks):
    viewtask(tasks)
    num=int(input("enter the task number you want to mark as completed "))
    if num <= len(tasks):
        tasks[num]["comp"]=True
        print("task marked as completed")
        print("\n")
    else :
        print("invalid task number")
        print("\n")


def delete(tasks):
    viewtask(tasks)
    num=int(input("enter the task number you want to delete"))
    if num <= len(tasks):
        del tasks[num]
        print("task deleted")
        print("\n")
    else :
        print("invalid task number")
        print("\n")


tasks=[]

while True :
    print("1.add task\n2.view task\n3.mark complete\n4.delete task\n5.exit")
    choice=int(input("enter your choice\t"))
    match choice :
        case 1:
            addtask(tasks)
        case 2:
            viewtask(tasks)
        case 3:
            markcomp(tasks)
        case 4:
            delete(tasks)
        case 5:
            print("exiting bye")
            break
        case _:
            print("invalid choice")
    
