# todo_cli.py - simple JSON-persisted to-do list
import json
import os

FILENAME = 'todo.json'

def load_tasks(filename=FILENAME):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks, filename=FILENAME):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(tasks, title):
    task = {'title': title, 'done': False}
    tasks.append(task)
    return tasks

def list_tasks(tasks):
    for i, t in enumerate(tasks, start=1):
        status = 'x' if t.get('done') else ' '
        print(f'{i}. [{status}] {t.get("title")}')

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        return True
    return False

if __name__ == '__main__':
    tasks = load_tasks()
    while True:
        print('\nTo-do CLI: (a)dd (l)ist (c)omplete (r)emove (q)uit')
        choice = input('Choose: ').strip().lower()
        if choice == 'a':
            title = input('Task title: ').strip()
            if title:
                add_task(tasks, title)
                save_tasks(tasks)
                print('Added.')
            else:
                print('Title required.')
        elif choice == 'l':
            list_tasks(tasks)
        elif choice == 'c':
            try:
                i = int(input('Task number to complete: ')) - 1
            except Exception:
                print('Invalid number')
            else:
                if complete_task(tasks, i):
                    save_tasks(tasks)
                    print('Marked complete.')
                else:
                    print('Invalid index')
        elif choice == 'r':
            try:
                i = int(input('Task number to remove: ')) - 1
            except Exception:
                print('Invalid number')
            else:
                if 0 <= i < len(tasks):
                    tasks.pop(i)
                    save_tasks(tasks)
                    print('Removed.')
                else:
                    print('Invalid index')
        elif choice == 'q':
            break
        else:
            print('Unknown option')
