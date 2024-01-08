import random

tasks = []


def add_task(description, priority=0):
    tasks.append({'description': description, 'priority': priority})
    print(f'Task "{description}" added successfully.') 


def view_tasks():
    if tasks:
        for i in tasks:
            print(i['priority'],i['description'])
    else :
        print("Task is not Present")







add_task()