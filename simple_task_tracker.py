import json
import os


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    # Load tasks from JSON file
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []

    # Save tasks to JSON file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Add Task
    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")

        task = {
            "title": title,
            "description": description
        }

        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!\n")

    # View Tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return

        print("\nYour Tasks:")
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
            choice = int(input("Enter task number to delete: "))
            if 1 <= choice <= len(self.tasks):
                removed = self.tasks.pop(choice - 1)
                self.save_tasks()
                print(f"Task '{removed['title']}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")


# Main Program
def main():
    manager = TaskManager()

    while True:
        print("===== Task Tracker =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.delete_task()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()