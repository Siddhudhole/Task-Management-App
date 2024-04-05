import pandas as pd 
import random
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report 

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


        
# Initialize for  traing data creation
    def train_data(self):
        data = pd.read_csv('task.csv')
        keyword ={'keyword':[]}
        for i in range(len(data)):

            words = data['description'][i].split() 
            if not words:
                return None  # Return None if the input text is empty
            keyword['keyword'].append(random.choice(words)) 
        data['keywords']=keyword['keyword']
        train_data = data[['description','keywords']]
        train_data.to_csv('train_data.csv',index=False)  

# Initialize for model training 
    
    def model_training(self):
        data = pd.read_csv('train_data.csv')
        x = data['keywords']
        y = data['description']

        # Convert keywords to numerical features using TF-IDF
        tfidf_vectorizer = TfidfVectorizer()
        X_train_tfidf = tfidf_vectorizer.fit_transform(x) 
        
    
        # Train a Naive Bayes classifier
        nb_classifier = MultinomialNB()
        nb_classifier.fit(X_train_tfidf,y)
        print(x)
        no_x = int(input("Enter number:")) 
        input_keyword = list(x[no_x]) 
        input_keyword_tfidf = tfidf_vectorizer.transform(input_keyword)  

        
        # Make predictions on the test set
        y_pred = nb_classifier.predict(input_keyword_tfidf) 
        print("Recommdated Task :-> ",y_pred[0])  

    def Recommdation():
        pass 
        
 


            
    
if __name__ == "__main__":

    object = Task_app() 
    while True :
        print("\nTask Management App")
        print("1. Add Task")
        print("2. List Task") 
        print("3. Remove Task")
        print("4. Recommendet Task")
        print("5. Priorit Task")
        print("6. Exit")


        choice = int(input("Enter Number :"))
        if choice == 1:
            object.add_task() 

        elif choice == 2:
            object.view_tasks()

        elif choice == 3 :
            object.remove_task()

        elif choice == 4:
             object.train_data() 
             object.model_training() 

        elif choice == 5 :
            object.priority_task()

        elif choice == 6 :
            break 

            
 
