class TaskManager:
    def __init__(self):
        self.tasks = []

    # Add Task
    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")

        task = {
            "title": title,
            "description": description
        }

        self.tasks.append(task)
        print("Task added successfully!\n")

    # View Tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return

        print("\n--- Your Tasks ---")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['title']} - {task['description']}")
        print()

    # Delete Task
    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete.\n")
            return

        self.view_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(self.tasks):
                removed = self.tasks.pop(task_num - 1)
                print(f"Task '{removed['title']}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")


# Main Program
def main():
    task_manager = TaskManager()

    while True:
        print("===== Task Tracker =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.delete_task()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()