# Git Release Demo

This tiny Python task-list app is intentionally simple so it can be used to
demonstrate merging changes from `dev` into `main`.

## Feature test list

- [x] Show a welcome message when the app starts
- [x] Add a task from user input
- [x] List tasks with numbers
- [x] Mark a task as complete
- [x] Remove a task
- [x] Save tasks to a file

Tasks are saved to `tasks.json` when the app exits and loaded again on the next
run. This makes the feature additions useful as a small follow-up release.

## Run it

```bash
python3 main.py
```

Use commands at the prompt:

- `add buy milk` adds a task
- `done 1` marks task 1 complete
- `remove 1` removes task 1
- `list` displays tasks
- `quit` saves and exits

Press Enter on an empty line to save and exit. The generated `tasks.json` file
is local demo data and can be deleted before a fresh run.
