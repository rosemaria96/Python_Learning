#TO DO LIST

todo_list = []

def addlist():
    item = input("Enter a new Task: ")
    todo_list.append((item))
    print(f"{item} added to the todo list")
def displaylist():
    print("---------")
    print("To Do List:")
    print("---------")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index} - {item}")
def removelist():
    displaylist()
    try:
        index = int(input("Enter your item number to remove: ")) - 1
        if 0 <= index < len(todo_list):
            removed_item = todo_list.pop(index)
            print(f"{removed_item} removed from the list")
        else:
            print("Invalid Input")
    except ValueError:
        print("Please enter a valid number")
    


while True:
    print("##############")
    print("To Do List App")
    print("##############")
    print("1 - Add to List")
    print("2 - Display List")
    print("3 - Remove From List")
    print("4 - Exit")

    option = input("Select your option")

    if option == '1':
        addlist()
    elif option == '2':
        displaylist()
    elif option == '3':
        removelist()
    elif option == '4':
        print("Exit")
        break
    else:
        print("Invalid Option")

    