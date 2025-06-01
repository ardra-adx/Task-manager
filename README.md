# Task-manager
 Python CLI Task Manager

A simple command-line task manager written in Python. You can add, edit, list, delete, and mark tasks as done using a few easy commands.

- Add new tasks with optional due dates
- Edit existing tasks
- Delete tasks
- Mark tasks as done
- List all tasks in a readable format
- Saves all tasks in a JSON file (`tasks.json`)

Flow:

1. Save the source code file as task_manager.py
2. Command:- To add a new task
   python task_manager.py add "Task Title" --due YYYY-MM-DD
   eg:- python task_manager.py add "Buy groceries" --due 2025-06-05
3. Command:- To edit a task
   python task_manager.py edit TASK_ID --title "New Title" --due YYYY-MM-DD
   eg:- python task_manager.py edit 1 --title "Buy milk" --due 2025-06-06
4. Command:- To delete a task
   python task_manager.py delete TASK_ID
   eg:- python task_manager.py delete 1
5. Command:- To mark a task as done
   python task_manager.py done TASK_ID
   eg :- python task_manager.py done 2
6. Command:- To list all tasks
   python task_manager.py list

All tasks are stored in a file named tasks.json in the same directory.



  





![Screenshot from 2025-05-30 01-18-29](https://github.com/user-attachments/assets/5c337bc2-49e4-4a5b-8308-0acd3a151a5a)
![Screenshot from 2025-05-30 01-18-43](https://github.com/user-attachments/assets/17dd2f18-5c54-45fd-b203-93185c0fe55d)
