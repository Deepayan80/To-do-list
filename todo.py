import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task: ").strip()

    if title == "":
        print("Task cannot be empty")
        return
    
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1

    task = {
        "id": new_id,
        "title": title,
        "done": False
    }

    tasks.append(task)
    print("Task added succesfully")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return
    
    print("============= Your Tasks ===============")

    for task in tasks:
        status = "Done" if task["done"] else "Pending"
        print(f'{task["id"]}.{task["title"]}[{status}]')

def update_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid input. Enter a number.")
        return

    # find task
    for task in tasks:
        if task["id"] == task_id:
            print("1. Edit Title")
            print("2. Mark as Done")
            print("3. Mark as Pending")

            choice = input("Choose option: ")

            if choice == "1":
                new_title = input("Enter new title: ").strip()
                if new_title == "":
                    print("Title cannot be empty.")
                    return
                task["title"] = new_title
                print("Task updated.")

            elif choice == "2":
                task["done"] = True
                print("Task marked as done.")

            elif choice == "3":
                task["done"] = False
                print("Task marked as pending.")

            else:
                print("Invalid choice.")

            return  # stop after updating

    print("Task ID not found.")

def delete_task(tasks):
    if len(tasks) == 0:
        print("No task available")
        return
    
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid input enter a number")
        return
    
    for i,task in enumerate(tasks):
        if task["id"] == task_id:
            confirm = input(f'Delete "{task["title"]}"? (y/n): ').lower()

            if confirm == "y":
                tasks.pop(i)
                print("Task deleted")
            else:
                print("Deletion cancelled")
            return
        
    print("Task ID not found")

def main():
    task = load_tasks()

    while True:
        print("============= To-Do List Menu ==============")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Update Tasks")
        print("4. Delete Tasks")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            #print("You selected add task")
            add_task(task)
            save_tasks(task)

        elif choice == 2:
            #print("You selected view task")
            view_tasks(task)

        elif choice == 3:
            #print("You selected update task")
            update_task(task)
            save_tasks(task)

        elif choice == 4:
            #print("You selected delete task")
            delete_task(task)
            save_tasks(task)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice try again")

if __name__ == "__main__":
    main()