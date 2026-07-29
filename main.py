"""A tiny task-list demo for practicing Git releases."""


def welcome_message():
    """Return the message shown when the app starts."""
    return "Welcome to the Demo Task List!"


def add_task(tasks, task):
    """Add a non-empty task and return the updated list."""
    task = task.strip()
    if task:
        tasks.append(task)
    return tasks


def list_tasks(tasks):
    """Return tasks as a numbered string."""
    if not tasks:
        return "No tasks yet."
    return "\n".join(f"{number}. {task}" for number, task in enumerate(tasks, start=1))


def main():
    tasks = []
    print(welcome_message())
    print("Type a task, or press Enter to finish.")

    while True:
        task = input("> ")
        if not task.strip():
            break
        add_task(tasks, task)

    print("\nYour tasks:")
    print(list_tasks(tasks))


if __name__ == "__main__":
    main()
