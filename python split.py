print('hi')
with open('expenses.txt','r') as f:
    for line in f:
        parts=line.strip().split('|')
print(parts)