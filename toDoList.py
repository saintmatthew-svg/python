tasks = []

def show_menu():
    output = """
            1. Add a task
            2. View all tasks
            3. Mark a task as complete
            4. Delete a task
            5. Exit
    """ 
    return output
    
print(show_menu())    

def add_task():
    todo = input("Add a task: ")
    tasks.append({'TASK': todo, 'STATUS': '[ ]'})
    return f"'{todo}' added to the list."
    
print(add_task())

def view_tasks():
    print('')
    print(' VIEW TASKS : ')
    for index in tasks:
        return (f"TASK: {index['STATUS']}{index['TASK']}")

print(view_tasks())
    
def mark_task_as_completed(tasks):
    view_tasks()
    task_index = int(input("Enter the task number to mark as complete: "))
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]['STATUS'] = '[X]'
        return f"Task: {tasks[task_index]['STATUS']} marked as complete."
    else:
        return "Invalid task number."

print(mark_task_as_completed(tasks))
    

