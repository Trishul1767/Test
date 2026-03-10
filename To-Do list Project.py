def view_tasks(tasks):
    if len(tasks)==0:
        print('Hurray!! No tasks pending')
    else:
        for i,j in enumerate(tasks):
            print(i+1,j)
def add_tasks(tasks):
    print('Note: type done to exist')
    print('Enter Tasks:')
    while True:
        b=input()
        if b.lower()=='done':
            break
        tasks.append(b)
    print("Pending Tasks:")
    for i,j in enumerate(tasks):
            print(i+1,j)
def remove_tasks(tasks,bin_tasks):
    print('Enter the number of the task to remove:\n')
    try:
        r=int(input())
        if r in range(1,len(tasks)+1):
            bin_tasks.append(tasks[r-1])
            print(f'{tasks[r-1]} is removed')
            tasks.pop(r-1)
            print('pending tasks:')
            for i,j in enumerate(tasks):
                print(i+1,j)
        else:
            print('there is no number representing the task')
    except ValueError:
        print('Please Enter Valid Number')
    
def removed_tasks(bin_tasks):
    if len(bin_tasks)==0:
        print('Empty Bin')
    else:
        print('Bin:')
        for i,j in enumerate(bin_tasks):
            print(i+1,j)
tasks=[]
bin_tasks=[]
print("  ********** Welcome to TO-DO list **********")
print('type 1 to view tasks')
print("type 2 to add tasks")
print('type 3 to remove tasks')
print('type 4 to see removed tasks')
print('type 5 to exit To-Do app!')
while True:
    try:
        n=int(input('enter a choice: '))
        if n==1:
            view_tasks(tasks)
        elif n==2:
            add_tasks(tasks)
        elif n==3:
            remove_tasks(tasks,bin_tasks)
        elif n==4:
            removed_tasks(bin_tasks)
        elif n==5:
            print('Thanks for using the app!')
            break
        else:
            print('invalid choice!')
    except ValueError:
        print('Please Enter Valid Number')