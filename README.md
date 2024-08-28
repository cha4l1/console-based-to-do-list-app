
# To-Do List Application v2.0

## Overview
This is the second version of a console-based To-Do List application written in Python. It allows users to manage their tasks with features like prioritization, scheduling, and completion tracking. The application stores tasks in a text file and offers options to import/export tasks, switch between different task modes, and save the task list.

## Features
- **Task Prioritization**: Categorize tasks into High, Medium, and Low priority levels.
- **Time-Based Sorting**: Sort tasks based on the scheduled time or deadline.
- **Task Completion**: Mark tasks as completed with a visual indicator.
- **File Management**: Import tasks from and export tasks to different text files.
- **Multiple Modes**: Switch between different task modes (e.g., schedule and to-do list).
- **Visual Feedback**: Colored output for better readability and user interaction.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required Python packages using pip:
   ```
   pip install termcolor
   ```
3. Download or clone this repository to your local machine.

## Usage
1. Navigate to the directory where the script is located.
2. Run the application using the following command:
   ```
   python todo_list_v2.py
   ```
3. Follow the on-screen instructions to add, delete, complete tasks, and more.

## Commands
- **Add a Task**: To add a new task, simply type the task description followed by the time (if any). For example:
  ```
  High: Buy groceries 15:00
  ```
- **Delete a Task**: To delete a task, use the command:
  ```
  delete [task_index]
  ```
  or
  ```
  del [task_index]
  ```
- **Complete a Task**: To mark a task as completed, use:
  ```
  complete [task_index]
  ```
- **Switch Modes**: To switch between schedule and to-do list modes:
  ```
  mode schedule
  ```
  ```
  mode todo-list
  ```
- **Import/Export Tasks**: To import tasks from a file or export tasks to a file:
  ```
  import [filename]
  ```
  ```
  export [filename]
  ```
- **Save Tasks**: To save the current list of tasks:
  ```
  save
  ```
- **Clear All Tasks**: To remove all tasks from the list:
  ```
  clear
  ```
- **Exit**: To exit the application:
  ```
  exit
  ```

## File Structure
- **data.txt**: Default file where tasks are stored.
- **schedule.txt**: Alternate file used when switching to schedule mode.

## Updates in v2.0
- Improved task sorting logic based on priority, time, and completion status.
- Enhanced visual feedback with colored outputs.
- Added multiple modes for better task management.
- Optimized task formatting and display.

## Contributing
If you have suggestions for improvements or find any issues, feel free to submit a pull request or open an issue on GitHub.

## License
This project is licensed under the MIT License.
