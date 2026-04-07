print('hi')
with open('expenses.txt','r') as f:
    for line in f:
        parts=line.split('|')
        print(parts)
