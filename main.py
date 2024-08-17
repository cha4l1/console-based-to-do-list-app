import os
from time import sleep
from termcolor import colored

# Set console to use UTF-8 encoding for proper character display
os.system('chcp 65001')

# Header bar for the To-Do List
header_bar = "******************** To-Do List ********************"
styled_header = colored(header_bar, "white", attrs=['bold'])

def center_text(string1, string2, offset=0):
    """
    Centers `string1` horizontally with respect to `string2`.

    Parameters:
    - string1 (str): The text to be centered.
    - string2 (str): The reference text whose length determines centering.
    - offset (int): Additional space to adjust centering.

    Returns:
    - str: A string with `string1` centered in relation to `string2`.
    """
    return " " * ((len(string2) - (len(string1) + offset)) // 2)

def display_error(text):
    """
    Displays an error message in red and waits for a short period.

    Parameters:
    - text (str): The error message to display.
    """
    error_message = colored(text, "red")
    print(center_text(error_message, header_bar, -9) + error_message)
    sleep(3)
    os.system("cls")  # Clear the console (use "cls" for Windows, "clear" for Unix-based systems)

def load_tasks():
    """
    Loads tasks from a file, creating the file if it doesn't exist.

    Returns:
    - list: A list of tasks loaded from the file, or an empty list if the file is empty or not found.
    """
    try:
        with open("data.txt", "r", encoding='utf-8') as file:
            content = file.read()
            content = content.split(", ")
            if content[0] == "":
                content = []
    except FileNotFoundError:
        with open("data.txt", "w+", encoding='utf-8') as file:
            file.write("")
            content = []
            
    return content

def save_tasks(tasks):
    """
    Saves the current list of tasks to a file.

    Parameters:
    - tasks (list): A list of tasks to be saved.
    """
    with open("data.txt", "w", encoding='utf-8') as file:
        file.write(', '.join(tasks))

def update_tasks(tasks, user_input):
    """
    Updates the list of tasks based on user input.

    Parameters:
    - tasks (list): The current list of tasks.
    - user_input (str): The user input command to update tasks.

    Returns:
    - list: The updated list of tasks.
    """
    command_parts = user_input.split(" ", 1)
    if command_parts[0].lower() in ["delete", "del"]:
        try:
            tasks.remove(tasks[int(command_parts[1]) - 1])
        except ValueError:
            display_error("Please enter a valid index of the task!")
        except IndexError:
            display_error("Please enter a correct index of the task!")
    elif command_parts[0].lower() == "complete":
        try:
            index = int(command_parts[1]) - 1
            tasks[index] = colored(f"{tasks[index]} √", "green")
        except ValueError:
            display_error("Please enter a valid index of the task!")
        except IndexError:
            display_error("Please enter a correct index of the task!")
    elif command_parts[0].lower() == "exit":
        return 0
    else:
        tasks.append(" ".join(command_parts))    
    return tasks

def run_program(tasks):
    """
    Runs the main loop of the program, displaying tasks and processing user input.

    Parameters:
    - tasks (list): The current list of tasks.

    Returns:
    - list or int: The updated list of tasks or 0 if the user wants to exit.
    """
    os.system("cls")  # Clear the console (use "cls" for Windows, "clear" for Unix-based systems)
    print(styled_header)
    if not tasks:
        noTasksMessage = colored("No tasks to display.", "yellow")
        print(center_text(noTasksMessage, styled_header) + noTasksMessage)
    for item in tasks:
        if "√" in item:
            print(center_text(item, header_bar, -9) + item)
        else:
            print(center_text(item, header_bar) + item)
    user_input = input("") 
    tasks = update_tasks(tasks, user_input) 
    return tasks

if __name__ == "__main__":
    # Main program loop
    while True:
        tasks = run_program(tasks)   
        if tasks == 0:
            os.system("cls")  # Clear the console
            break

    save_tasks(tasks)
