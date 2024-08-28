import os
from time import sleep
from termcolor import colored
from datetime import datetime
import re

os.system('chcp 65001')
os.system('mode con:cols=76')

FILE = "data.txt"
header_bar = "  ****************************** To-Do List ******************************  "
styled_header = colored(header_bar, "yellow")
priority_color = {"High": "red", "Medium" : "yellow", "Low": "white"}


############################### HELPER FUNCTIONS ###############################
def center_text(string1, string2, offset=0): # Centers string1 according to string 2
    return " " * ((len(string2) - (len(string1) + offset)) // 2)

def display_message(text, freeze_time=3, color="red"): #displays message
    message = colored(text, color)
    print(center_text(message, header_bar, -9) + message)
    sleep(freeze_time)  
    os.system("cls") 
    
    
############################### SORING TASKS ###############################
def extract_priority(task):
    if "High" in task:
        return 0
    elif "Medium" in task:
        return 1
    else:
        return 2

def extract_time(task):
    # hours = datetime.now().hour
    # minutes = datetime.now().minute
    schedule_exp = re.search("\d+\:\d+\-\d+\:\d+", task)
    deadline_exp = re.search("\d+\:\d+", task)
    if schedule_exp:
        time = schedule_exp.group().split("-")[1].split(":")
    elif deadline_exp:
        time = deadline_exp.group().split(":")
    else:
        time = [24, 1] # bigger than one day for put this at the bottom of list
        
    return int(time[0])*60 + int(time[1])
        
def extract_completed(task):
    return colored('√', "green") in task 

def sort_task(task):
    return (extract_priority(task), extract_time(task), extract_completed(task))
    


############################### RELATED WITH TASK ###############################
def change_file_direction(action, file, tasks):
    global FILE
    if ".txt" in file:
        FILE = file
        if action == "import":
            tasks = load_or_save_tasks("import", tasks)
        elif action == "export":
            load_or_save_tasks("export", tasks)
    else:
        display_message("Please enter correct file. (EX: data.txt)")

    return tasks

def load_or_save_tasks(action, tasks=None):
    if action == "import":
        try:
            with open(FILE, "r", encoding='utf-8') as file:
                content = file.read()
                content = content.split(", ")
                if content[0] == "":
                    content = []
        except FileNotFoundError:
            with open(FILE, "w+", encoding='utf-8') as file:
                file.write("")
                content = []
        return content
    elif action == "export":
        with open(FILE, "w", encoding='utf-8') as file:
            file.write(', '.join(tasks))
        return 0
    
def priority_tasks(tasks, priority_level_group):
    for task in tasks:
        if "High" in task:
            priority_level_group["High"].append(task)
        elif "Medium" in task:
            priority_level_group["Medium"].append(task)
        else:
            priority_level_group["Low"].append(task)
            
    return priority_level_group
    

def format_task(command_parts, tasks):
    priority = command_parts[0].split(":")[0]
    time = command_parts[-1]
    if priority in ["High", "Medium"]:
        command_parts[0] = colored(f"[{priority}]", priority_color[priority])
        command_parts[-1] = colored(f"[{time}]", "magenta") if ":" in time else command_parts[-1]
    elif ":" in time:
        command_parts[-1] = colored(f"[{time}]", "magenta")
    
    formatted_task = " ".join(command_parts)
    
    return formatted_task

def complete_task(task):
    task_parts = task.split(" ")
    start = task_parts[0]
    end = task_parts[-1]

    if "\x1b" in start:
        if "\x1b" in end:
            return start + colored(f" {' '.join(task_parts[1:-1])} √ ", "green") + end
        return start + colored(f" {' '.join(task_parts[1:])} √", "green")
    elif "\x1b" in end:
        return colored(f"{' '.join(task_parts[:-1])} √ ", "green") + end
    else:
        return colored(f"{' '.join(task_parts)} √", "green")

def update_tasks(tasks, user_input):
    command_parts = user_input.split(" ")
    action = command_parts[0].lower()
    if action in ["delete", "del"]:
        try:
            tasks.remove(tasks[int(command_parts[1]) - 1])
        except (ValueError, IndexError):
            display_message("Please enter correct index of task!")
    elif action == "complete":
        try:
            index = int(command_parts[1]) - 1
            tasks[index] = complete_task(tasks[index])
        except (ValueError, IndexError):
            display_message("Please enter correct index of task!")
    elif action == "clear":
        tasks = []
    elif action == "mode":
        if command_parts[1] == "schedule":
            load_or_save_tasks("export", tasks)
            tasks = change_file_direction("import", "schedule.txt", tasks)
        elif command_parts[1] == "todo-list":
            load_or_save_tasks("export", tasks)
            tasks = change_file_direction("import", "data.txt", tasks)
    elif action in ["import", "export"]:
        tasks = change_file_direction(action, command_parts[1], tasks)
    elif action == "save":
        load_or_save_tasks("export", tasks)
        display_message("Tasks saved successfully!", 2, "green")
    elif action == "exit":
        return 0
    else:
        tasks.append(format_task(command_parts, tasks))
    return tasks




############################### MAIN ###############################

def run_program(tasks):
    priority_level_group = {"High": [], "Medium": [], "Low": []}
    os.system("cls")
    print(styled_header)
    if tasks == []:
        noTasksMessage = colored("No tasks to display.", "light_yellow")
        print(center_text(noTasksMessage, styled_header) + noTasksMessage)
    
    tasks.sort(key = lambda task: (sort_task(task)[0], sort_task(task)[1], not sort_task(task)[2]))
    priority_level_group = priority_tasks(tasks, priority_level_group)
    
    for level in priority_level_group:
        for item in priority_level_group[level]:    
            offset = item.count("\x1b") // 2 * (-9)
            if "√" in item:
                print(center_text(item, header_bar, offset) + item)
            else:
                print(center_text(item, header_bar, offset) + item)
    # print(tasks) 
    user_input = input("") 
    tasks = update_tasks(tasks, user_input)
    return tasks

def main():
    tasks = load_or_save_tasks("import")
    while True:
        var = run_program(tasks)   
        if var == 0:
            os.system("cls")
            break
        tasks = var
    load_or_save_tasks("export", tasks)

if __name__ == "__main__":
    main()
