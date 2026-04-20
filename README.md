# 📌 Simple Task Tracker (Python)

## 📖 Overview
The **Simple Task Tracker** is a basic Python application that allows users to manage their daily tasks. Users can add, view, and delete tasks using a simple menu-driven interface.

This project is built using object-oriented programming (OOP) concepts in Python.

---

## 🎯 Objective
To create a simple command-line task manager using:
- Python classes
- Lists for data storage
- User input handling
- Loop-based menu system

---

## ⚙️ Features
✔️ Add Task  
✔️ View Tasks  
✔️ Delete Task  

---

## 🧱 Task Structure
Each task is stored as a dictionary:

```python
{
    "title": "Study Python",
    "description": "Finish basics"
}
````

---

## 🗂️ Data Storage

* Tasks are stored in a list:

```python
self.tasks = []
```

* JSON file support is optional (bonus feature)

---

## 🧩 Class Used

```python
class TaskManager:
```

---

## 🖥️ Menu System

The program displays:

```
===== Task Tracker =====

1. Add Task
2. View Tasks
3. Delete Task
4. Exit
```

---

## 🔄 Sample Usage

```
Enter choice: 1
Enter Title: Study Python
Enter Description: Finish loops
Task added successfully!
```

---

## 🚀 How to Run

1. Make sure Python is installed
2. Clone this repository:

```
https://github.com/yeaminhossainfuhad-cloud/Simple_Task_Tracker.git
```

3. Navigate to the folder:

```
 cd .\Simple_Task_Tracker\
```

4. Run the program:

```
python simple_task_tracker.py
```

---

## 📝 Basic Rules Followed

* Used a class (`TaskManager`)
* Used functions inside the class
* Used `input()` for user interaction
* Used loops to keep the program running

---

## 💡 Future Improvements (Optional)

* Save tasks to a JSON file
* Add task update feature
* Add priority levels
* Add deadline/reminder system

---

## 👨‍💻 Author

Md Yeamin Hossain Fuhad
---
