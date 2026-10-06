tasks=[]
def show_menu():
    print("--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Task ")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exist")
def add_task():
        task=input("Enter task:")
        tasks.append({"task":task,"done":False})
        print(f"Task'{task}'added!")

def View_task():
        if not tasks:
            print("No tasks yet!")
            return
        print("/nYour Tasks:")
        for index, task in enumerate(tasks,start=1):
            status="✅ " if task["done"] else "❌"
            print(f"{index}. {task['task']} [{status}]")

def mark_done():
        View_task()
        if not tasks:
            return
        try:
            index=int(input("Enter task number to mark done:")) - 1 
            if 0 <=index < len(tasks):
                tasks[index]["done"]= True
                print("marked as done!")
            
            else:
                print("Invalid number!")
        except ValueError:
            print("please enter a valid number.")

def delete_task():
        View_task()
        if not tasks:
            return
        try:
            index=int(input("Enter task number to delete:"))-1
            if 0<= index <len(tasks):
                removed= tasks.pop(index)
                print(f"Deleted task:{removed['task']}")
            else:
                print("Invalid number!")
        except ValueError:
            print("please enter a valid number.")

while True:
        show_menu()
        choice=input("choose an option(1-5):")

        if choice =='1':
            add_task()
        elif choice=='2':
            View_task()
        elif choice=='3':
            mark_done()
        elif choice=='4':
            delete_task()
        elif choice=='5':
            print("goodbye!")
            break
        else:
            print("Invalloid choice.Try agaun.")

               