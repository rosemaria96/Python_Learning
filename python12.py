tasks = []

def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def add_task():
    task_name = input("Enter new task: ")
    tasks.append({'task': task_name, 'done': False})
    print("Task added!")

def mark_completed():
    view_tasks()
    task_num = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['done'] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
