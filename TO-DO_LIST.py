def show_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added to the to-do list.")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task.strip()}' removed from the to-do list.")
    else:
        print("Invalid task index.")

def update_task(tasks, task_index, new_task):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_task
        print(f"Task updated to '{new_task}' in the to-do list.")
    else:
        print("Invalid task index.")

def main():
    tasks = []

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Update task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            update_task(tasks, task_index, new_task)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
