def showMenu():
    print("Todo List Menu:")
    print("1 - View all tasks")
    print("2 - Add task")
    print("3 - Remove task")
    print("4 - Mark Task as Complete")
    print("5 - Exit")

def viewTasks(tasks: list):
    if tasks:
        print("Todo List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {'[x]' if task['completed'] else '[]'} {task['task']}")
    else:
        print("No tasks in the task list.")

def addTask(tasks: list, task: str):
    tasks.append({"task": task, "completed": False})

def removeTask(tasks:list, taskIndex: int):
    del tasks[taskIndex]

def completeTask(tasks: list, taskIndex: int):
    tasks[taskIndex]["completed"] = True

def main():
    tasks = []
    userChoice = int(input("1 - Start App | 2 - Stop App: "))
    while userChoice != 2:
        showMenu()
        userInput = int(input("Enter choice (1-5): "))
        if userInput == 1:
            viewTasks(tasks)
        elif userInput == 2:
            newTask = input("Enter task that you want to add to the list: ")
            addTask(tasks, newTask)
            print("Task added successfully!")
        elif userInput == 3:
            removeIndex = int(input("Enter the index of the task which you would like to remove: ")) - 1
            removeTask(tasks, removeIndex)
            print("Task removed successfully!")
        elif userInput == 4:
            markTask = int(input("Enter the index of the task which you would like to mark as completed: ")) - 1
            completeTask(tasks, markTask)
            print("Task completed successfully!")
        elif userInput == 5:
            print("Exiting...")
            break
        userChoice = int(input("1 - Continue | 2 - Stop App: "))
main()
print("Exiting...")