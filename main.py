import random

tasks = []


def add_task(description, priority=0):
    tasks.append({'description': description, 'priority': priority})
    print(f'Task "{description}" added successfully.')