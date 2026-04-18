import os
os.path.exists('student.txt')
if os.path.exists('student.txt'):
    with open('student.txt','r') as f:
        print(f.read())
else:
    print("File not found.")