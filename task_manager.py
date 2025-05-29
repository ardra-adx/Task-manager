import argparse
import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "" if task["done"] else ""
        due = task.get("due", "No due date")
        print(f"[{task['id']}] {status} {task['title']} (Due: {due})")

# Add a new task
def add_task(title, due):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {
        "id": task_id,
        "title": title,
        "done": False,
        "due": due
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")

# Edit a task
def edit_task(task_id, title=None, due=None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if due:
                task["due"] = due
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print(f"Task {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task {task_id} deleted.")

# Mark a task as done
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task {task_id} not found.")

# Main function to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="Python CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("title", help="Title of the task")
    parser_add.add_argument("--due", help="Due date (YYYY-MM-DD)", default="No due date")

    # Edit command
    parser_edit = subparsers.add_parser("edit")
    parser_edit.add_argument("id", type=int, help="Task ID")
    parser_edit.add_argument("--title", help="New title of the task")
    parser_edit.add_argument("--due", help="New due date")

    # Delete command
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("id", type=int, help="Task ID")

    # Mark as done
    parser_done = subparsers.add_parser("done")
    parser_done.add_argument("id", type=int, help="Task ID")

    # List tasks
    subparsers.add_parser("list")

    args = parser.parse_args()

    # Command routing
    if args.command == "add":
        add_task(args.title, args.due)
    elif args.command == "edit":
        edit_task(args.id, args.title, args.due)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
