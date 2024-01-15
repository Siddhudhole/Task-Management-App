import random
import pandas as pd 

# Initialize dataframe for reference


# Initialize an empty task list
tasks = {'description':[],'priority':[]}

# read exiting csv file
try :
    tasksdf = pd.read_csv('tasks.csv')
except FileNotFoundError:
    pass 


# Function to save tasks to a CSV file
def save_tasks():
    tasksdf.to_csv('task.csv', index=False) 

# Initialize for add tasks
def add_task(description, priority):
    global tasks 
    global tasksdf
    tasks['description'].append(description)
    tasks['priority'].append(priority)
    print(f'Task "{description}" added successfully.') 
    new_tasks = pd.DataFrame(tasks)
    tasksdf = pd.concat([tasksdf,new_tasks],ignore_index=True)
    tasksdf.to_csv('task.csv')
     

# Initialize for view all tasks
def view_tasks():
    if tasks:
        for i in tasks['description']:
            print(i) 
        
    else:
        print("No tasks available.") 

# Initialize for modify tasks
def modify_task(x):
    if x>= len(tasks['description']):
       tasks['description'][x-1]=input('Enter a new task :')
       print("sucessfully modify task :",tasks["description"][x-1])
    else : 
        print("enter valid input ") 

# Initialize for remove tasks
def remove_task():
    if tasks:
        view_tasks()
        x = int(input("Enter Number :"))
        del tasks['description'][x-1]
        del tasks['priority'][x-1]
        print('remove succesfully ')
    else :
        print("Tasks Not Present !")


while True :
    print("\nTask Management App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. modify task")
    print("5. Exit")
    try :

       choice =int(input("Enter Your choice : "))
    except :
        print("Plz Enter a Number") 

    if choice == 1 :
        try :
            desc = input("Enter Description : ")
            prio = input("Enter Priority Low/High/Medium : ")
            add_task(desc,prio.upper())

        except :
            print("Enter valid description & priority")

    elif choice == 2:
        remove_task()
  

    elif choice == 3 :
        view_tasks()

    elif choice == 4 :
        view_tasks()
        x = int(input("Enter a number present the task : "))
        modify_task(x) 
         

    elif choice == 5:
        break 