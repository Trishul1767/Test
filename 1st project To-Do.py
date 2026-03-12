import os
def load_tasks():
    f={}
    if os.path.exists('tasks.txt'):
        with open('tasks.txt','r') as file:
            for line in file:
                task,status=line.strip().rsplit(' | ',1) 
                f[task]=status
    return f

def load_bin_tasks():
    bin_tasks=[]
    if os.path.exists('bin.txt'):
        with open('bin.txt','r') as file:
            for line in file:
                bin_tasks.append(line.strip())
    return bin_tasks

def file_code(f):
    with open('tasks.txt','w') as file:
        for i,j in f.items():
            file.write(f'{i} | {j}\n')

def iterate_tasks(f):
    a=1
    for i,j in f.items():
        if j=='done':
            print(f'{a}. {i} | [✓]')
        else:
            print(f'{a}. {i} | [ ]')
        a+=1

def view_tasks(f):
    if len(f)==0:
        print('Hurray!! No tasks.')
    else:
        iterate_tasks(f)

def add_tasks(f):
    print('Note: type done to exit')
    print('Enter Tasks:')
    with open('tasks.txt','a') as file:
        while True:
            b=input().strip()
            if b=='':
                print('Task cannot be empty')
                continue
            if b.lower()=='done':
                break
            elif b in f:
                c=1
                while b+str(c) in f:
                    c+=1
                f[b+str(c)]='pending'
                file.write(f'{b+str(c)} | pending\n')
            else:
                f[b]='pending'
                file.write(f'{b} | pending\n')
        iterate_tasks(f)

def update_tasks(f):
    print('note: type 0 if done')
    if len(f)==0:
        print('No tasks to update')
    else:
        iterate_tasks(f)
        try:
            while True:
                r=int(input())
                if r==0:
                    break
                elif 'peding' not in f.values():
                    break
                elif r in range(1, len(f) + 1):
                    keys1=list(f.keys())
                    f[keys1[r-1]]='done'
                    print('Update Complete')
                    iterate_tasks(f)
                    file_code(f)
                else:
                    print('Invalid task number')
        except ValueError:
            print('Please Enter Valid Number')

def view_done_tasks(f):
    print('Done tasks: ')
    a=1
    if 'done' not in f.values():
        print('No tasks done yet!')
    else:
        for i,j in f.items():
            if j=='done':
                print(f'{a}. {i}')
                a+=1

def view_pending_tasks(f):
    print('Pending tasks: ')
    a=1
    if 'pending' not in f.values():
        print('No pending tasks!')  
    else:
        for i,j in f.items():
            if j=='pending':
                print(f'{a}. {i}')
                a+=1
    
def search_tasks(f):
    s=input('Enter the task to search: ').strip()
    flag=False
    for i,j in f.items():
        if s.lower() in i.lower():
            print(f'{i} | {j}')
            flag=True
    if not flag:
        print('Task not found')

def remove_tasks(f,bin_tasks):
    print('Enter the number of the task to remove:\n')
    iterate_tasks(f)
    print("Note: type '0' if done")
    if len(f)==0:
        print('No tasks to remove')
    else:
        try:
            while True:
                r=int(input())
                if r==0:
                    break
                elif len(f)==0:
                    break
                elif r in range(1, len(f) + 1):
                    keys1=list(f.keys())
                    bin_tasks.append(keys1[r-1])
                    with open('bin.txt','a') as file:
                        file.write(f'{keys1[r-1]}\n')
                    print(f'{keys1[r-1]} is removed')
                    f.pop(keys1[r-1])
                    print('Tasks:')
                    iterate_tasks(f)
                    file_code(f)
                else:
                    print('Invalid task number')
            print('Tasks:')
            iterate_tasks(f)
            file_code(f)
        except ValueError:
            print('Please Enter Valid Number')
    
def removed_tasks(bin_tasks):
    if len(bin_tasks)==0:
        print('Empty Bin')
    else:
        print('Bin:')
        for i,j in enumerate(bin_tasks):
            print(f'{i+1}. {j}')

def empty_bin(bin_tasks):
    bin_tasks.clear()
    with open('bin.txt','w') as file:
        file.write('')
    print("Bin Emptied.")

bin_tasks=load_bin_tasks()
f=load_tasks()
print("  ********** Welcome to TO-DO list **********")
print('type 1 to view tasks')
print("type 2 to add tasks")
print('type 3 to update tasks')
print('type 4 to see done tasks')
print('type 5 to see pending tasks')
print('type 6 to search tasks')
print('type 7 to remove tasks')
print('type 8 to see removed tasks')
print('type 9 to empty bin')
print('type 10 to exit To-Do app!')
while True:
    try:
        n=int(input('enter a choice: '))
        if n==1:
            view_tasks(f)
        elif n==2:
            add_tasks(f)
        elif n==3:
            update_tasks(f)
        elif n==4:
            view_done_tasks(f)
        elif n==5:
            view_pending_tasks(f)
        elif n==6:
            search_tasks(f)
        elif n==7:
            remove_tasks(f,bin_tasks)
        elif n==8:
            removed_tasks(bin_tasks)
        elif n==9:
            empty_bin(bin_tasks)
        elif n==10:
            print('Thanks for using the app!')
            break
        else:
            print('invalid choice!')
    except ValueError:
        print('Please Enter Valid Number')