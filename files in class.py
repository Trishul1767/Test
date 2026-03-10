n=int(input('Enter number of students: '))
students=[]
for i in range(n):
    d={}
    d['name']=input('Enter name: ')
    d['age']=int(input('Enter age: '))
    d['grade']=input('Enter grade: ')
    students.append(d)


with open('student.txt','w+') as f:
    for s in students:
        f.write(str(s)+'\n')
    f.seek(0)
    print(f.read())
print('student details stored successfully')