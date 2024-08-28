
# To-Do List Application - Version 2

## Introduction
This is the second version of a command-line To-Do List application. It allows users to manage their tasks by adding, deleting, completing, and prioritizing tasks. The application also supports saving and loading tasks to and from a text file.

## Features
- **Task Prioritization:** Tasks can be categorized as High, Medium, or Low priority.
- **Task Sorting:** Tasks are automatically sorted based on priority and time.
- **Task Completion:** Tasks can be marked as completed.
- **Task File Management:** Import and export tasks to different files.
- **Color-coded Output:** Priority levels and completed tasks are color-coded for better readability.

## Usage

### Adding a Task
To add a task, simply type the task details in the format:

```
<Priority>: <Task Description> <Time (Optional)>
```

Example:
```
High: Finish homework 18:00
```

### Completing a Task
To mark a task as completed, type:

```
complete <task number>
```

Example:
```
complete 1
```

### Deleting a Task
To delete a task, type:

```
delete <task number>
```

Example:
```
delete 2
```

### Changing Modes
Switch between different modes (files) with:

```
mode <schedule/todo-list>
```

Example:
```
mode schedule
```

### Saving Tasks
To save the current list of tasks to the file, type:

```
save
```

### Exiting the Program
To exit the program, type:

```
exit
```

## Files
- **data.txt**: The default file where tasks are stored.
- **schedule.txt**: An alternative file for storing tasks.

## Requirements
- Python 3.x
- `termcolor` module

You can install the required module using pip:

```
pip install termcolor
```

## Running the Application
To run the application, execute the script:

```
python todo_list.py
```

## Notes
- Ensure that the terminal is set to UTF-8 encoding for proper display of colored text.
- The application adjusts the console window size automatically for optimal display.

## Version History
- **Version 1:** Initial release with basic task management features.
- **Version 2:** Added task prioritization, sorting by time, and improved task completion logic.
