"""A tiny task-list demo for practicing Git releases."""

import json
from pathlib import Path


def welcome_message():
    """Return the message shown when the app starts."""
    return "Welcome to the Demo Task List!"


def add_task(tasks, task):
    """Add a non-empty task and return the updated list."""
    task = task.strip()
    if task:
        tasks.append({"text": task, "completed": False})
    return tasks


def list_tasks(tasks):
    """Return tasks as a numbered string, showing completion state."""
    if not tasks:
        return "No tasks yet."
    return "\n".join(
        f"{number}. [{'x' if task['completed'] else ' '}] {task['text']}"
        for number, task in enumerate(tasks, start=1)
    )


def complete_task(tasks, number):
    """Mark a numbered task complete. Return whether the task was found."""
    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        return True
    return False


def remove_task(tasks, number):
    """Remove a numbered task and return whether the task was found."""
    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        return True
    return False


def save_tasks(tasks, filename="tasks.json"):
    """Save tasks as human-readable JSON."""
    Path(filename).write_text(json.dumps(tasks, indent=2) + "\n", encoding="utf-8")


def load_tasks(filename="tasks.json"):
    """Load tasks from JSON, returning an empty list when no file exists."""
    path = Path(filename)
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    tasks = load_tasks()
    print(welcome_message())
    print("Commands: add <task>, done <number>, remove <number>, list, quit")

    while True:
        command = input("> ").strip()
        if not command:
            break
        action, _, value = command.partition(" ")
        action = action.lower()

        if action in {"quit", "exit"}:
            break
        if action == "add" and value.strip():
            add_task(tasks, value)
        elif action == "done":
            try:
                if not complete_task(tasks, int(value)):
                    print("That task number does not exist.")
            except ValueError:
                print("Usage: done <number>")
        elif action == "remove":
            try:
                if not remove_task(tasks, int(value)):
                    print("That task number does not exist.")
            except ValueError:
                print("Usage: remove <number>")
        elif action == "list":
            print(list_tasks(tasks))
        else:
            print("Usage: add <task>, done <number>, remove <number>, list, quit")

    save_tasks(tasks)
    print("\nYour tasks:")
    print(list_tasks(tasks))


if __name__ == "__main__":
    main()
