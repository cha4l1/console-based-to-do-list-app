import os
from time import sleep
from termcolor import colored

os.system('chcp 65001')

header_bar = "******************** To-Do List ********************"
styled_header = colored(header_bar, "white", attrs=['bold'])

def center_text(string1, string2, offset=0):
    return " " * ((len(string2) - (len(string1) + offset)) // 2)

def display_error(text):
    error_message = colored(text, "red")
    print(center_text(error_message, header_bar, -9)  + error_message)
    sleep(3)
    os.system("delete 0")
    
def load_tasks():
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
    with open("data.txt", "w", encoding='utf-8') as file:
        file.write(', '.join(tasks))
            
def update_tasks(tasks, user_input):
    command_parts = user_input.split(" ", 1)
    if command_parts[0].lower() == "delete" or command_parts[0].lower() == "del":
        try:
            tasks.remove(tasks[int(command_parts[1]) - 1])
        except ValueError:
            display_error("Please enter index of task!")
        except IndexError:
            display_error("Please enter correct index of task!")
    elif command_parts[0].lower() == "complete":
        try:
            index = int(command_parts[1]) - 1
            tasks[index] = colored(f"{tasks[index]} √",  "green")
        except ValueError:
            display_error("Please enter index of task!")
        except IndexError:
            display_error("Please enter correct index of task!")
    elif command_parts[0].lower() == "exit":
        return 0
    else:
        tasks.append(" ".join(command_parts))    
    return tasks
        
tasks = load_tasks()

def run_program(tasks):
    os.system("cls")
    print(styled_header)
    if tasks == []:
        noTasksMessage = colored("No tasks to display.", "yellow")
        print(center_text(noTasksMessage, styled_header) + noTasksMessage)
    for item in tasks:
        if item.find("√") != -1:
            print(center_text(item, header_bar, -9)  + item)
        else:
            print(center_text(item, header_bar)  + item)
    user_input = input("") 
    tasks = update_tasks(tasks, user_input) 
    return tasks

if __name__ == "__main__":
    while True:
        var = run_program(tasks)   
        if var == 0:
            os.system("cls")
            break
        tasks = var

save_tasks(tasks)
