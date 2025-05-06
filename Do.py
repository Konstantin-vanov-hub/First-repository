import os
Tasks = []

class Task:
    def __init__(self, title, priorety, status):
        self.title = title
        self.priorety = priorety
        self.status = status
    
    def info(self):
        print(f'Task:{self.title}, Priorety:{self.priorety}, Status:{self.status}')

    def to_string(self):
        return(f'Task:{self.title}, Priorety:{self.priorety}, Status:{self.status}')

print('1. List of tasks(list): \n' 
      '---------------------- \n'
      '2. Add new task(add): \n'
      '---------------------- \n' 
      '3. Del the task(del): \n'
      '---------------------- \n' 
      '4. New status(newst): \n'
      '---------------------- \n' 
      '5. New priorety(newpr): \n' 
      '---------------------- \n'
      '6. New title of task(newt): \n'
      '---------------------- \n'  
      '7. Exit(exit): \n')  

if os.path.exists('C:\\Users\\Computer\\Desktop\\Tasks.txt'):
    with open('C:\\Users\\Computer\\Desktop\\Tasks.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            title = parts[0].split(':')[1]
            priorety = parts[1].split(':')[1]
            status = parts[2].split(':')[1]
            Tasks.append(Task(title, priorety, status))

while True:
    command = input('Enter the command: ')
    if command == 'list':
        for i in Tasks:
             i.info()

    if command == 'add':
        while True:
            new_task = input('Enter the new task: ')
            if new_task == 'break':
                break
            new_priorety = input('Enter the new priorety: ')
            new_status = input('Enter the new status: ')
            Task0 = Task(new_task, new_priorety, new_status)
            Tasks.append(Task0)

    if command == 'del':
        while True:
            del_element = input('Enter the task to del: ')
            if del_element == 'break':
                break
            for i in Tasks:
                if i.title == del_element:
                    Tasks.remove(i)
    
    if command == 'newst':
        while True:
            task_status1 = input('Enter the task: ')
            if task_status1 == 'break':
                break
            new_status1 = input('Enter the new status: ')
            for i in Tasks:
                if task_status1 == i.title:
                    i.status = new_status1 

    if command == 'newpr':
        while True:
            task_priorety1 = input('Enter the task: ')
            if task_priorety1 == 'break':
                break
            new_priorety1 = input('Enter the new priorety: ')
            for i in Tasks:
                if i.title == task_priorety1:
                    i.priorety = new_priorety1

    if command == 'newt':
        while True:
            new_title1 = input('Enter the title: ')
            if new_title1 == 'break':
                break
            new_title = input('Enter the new title: ')
            for i in Tasks:
                if i.title == new_title1:
                    i.title = new_title

    if command == 'exit':
        with open('C:\\Users\\Computer\\Desktop\\Tasks.txt','w') as file:
            for i in Tasks:
                file.write(i.to_string() +'\n')

        break

