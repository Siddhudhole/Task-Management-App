import pandas as pd 
class Task_app:
    tasks = {'description':[],'priority':[]}
# Read old tasks 
    try :
        old_tasks = pd.read_csv('task.csv')
        old_tasks =pd.DataFrame(old_tasks)
    except FileNotFoundError:
        pass
        
        
    
    # Initialize for add tasks
    def add_task(self):
        while True:
            x = (input("add new task Yes or Not: "))
            x = x.upper()
            if x =='YES':


                description = input("Enter description :")
                priority = input("Enter priority : ")
                priority =priority.upper()
                object.tasks['description'].append(description)
                object.tasks['priority'].append(priority) 
                new_tasks = pd.DataFrame(object.tasks) 
            else :
                break 
        try :

            object.tasks = pd.concat([object.old_tasks,new_tasks],ignore_index=True)
            object.tasks.to_csv('task.csv',index=False)
            

        
        except :
            new_tasks.to_csv('task.csv') 



 # Initialize for list tasks   
    def view_tasks(self):
        tasks = pd.read_csv('task.csv')
        if tasks.empty:
             print('Task is Not present !')
           
        else :
            task = list(tasks['description'][:])
            for i in task :
                print(i)  

# Initialize for remove tasks 
    def remove_task(self):
        task = pd.read_csv('task.csv')

        if task.empty :
            print("Task Is not Present !")
        else :
            object.view_tasks()
            x = int(input("Enter Number task is present :"))
            if x <= len(task):
                task = task.drop(x-1)
                task.to_csv('task.csv') 
                print("Successfully remove Task !") 
            else :
                print("Enter invalid input ! ") 

            
           
             
    
if __name__ == "__main__":

    object = Task_app() 
    while True :
        print("\nTask Management App")
        print("1. Add Task")
        print("2. List Task") 
        print("3. Remove Task")


        choice = int(input("Enter Number :"))
        if choice == 1:
            object.add_task() 

        elif choice == 2:
            object.view_tasks()

        elif choice == 3 :
            object.remove_task()
 