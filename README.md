
# To-Do List Application

This is a simple command-line To-Do List application that helps you manage your tasks effectively. It allows you to add, complete, and delete tasks, providing a straightforward and user-friendly experience.

## Features

- **Add Tasks:** Simply type your task to add it to the list.
- **Delete Tasks:** Use the `delete` command followed by the task number to remove it.
- **Complete Tasks:** Use the `complete` command followed by the task number to mark it as completed. Completed tasks will be shown in green with a checkmark (√).
- **Persistent Storage:** All tasks are saved to a file (`data.txt`) and loaded each time the application starts.

## Usage

### Running the Application

1. Make sure you have Python installed on your machine.
2. Install the required package by running:  
   ```
   pip install termcolor
   ```
3. Run the application with:
   ```
   python main.py
   ```

### Commands

- **Add a Task:** Just type the task and press Enter.  
  Example:  
  ```
  Buy groceries
  ```

- **Complete a Task:**  
  ```
  complete 1
  ```

- **Delete a Task:**  
  ```
  delete 1
  ```

- **Exit the Application:**  
  ```
  exit
  ```

## Notes

- The application handles errors such as entering an invalid task number by displaying an appropriate error message.
- The tasks are saved in a text file (`data.txt`) in the application's directory. Ensure this file is in the correct location when running the script.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
