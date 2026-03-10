''' to add one student details to a file
def add_student():
    name=input('Enter name: ')
    age=int(input('Enter age: '))
    grade=input('Enter grade: ')
    student={'name':name,'age':age,'grade':grade}
    with open('student.txt','a') as f:
        f.write(str(student)+'\n')
    print('Student details stored successfully')'''
while True:
    print('enter 1 to add number of student details')
    print('type 2 to view student details')
    print('type 3 to view student details')
    print('type 4 to exit')
    n=int(input())
    if n==1:
        n=int(input('Enter number of students: '))
        students=[]
        for i in range(n):
            d={}
            d['name']=input('Enter name: ')
            d['roll']=int(input('Enter roll: '))
            d['grade']=input('Enter grade: ')
            students.append(d)


        with open('student.txt','w+') as f:
            for s in students:
                f.write(str(s)+'\n')
            f.seek(0)
            print(f.read())
        print('student details stored successfully')
    elif n==2:
        n=int(input('enter the roll number of the student: '))
        with open('student.txt','r') as f:
            for line in f:
                student=eval(line)
                if student['roll']==n:
                    print(student)
                    break
            else:
                print('student not found')
    elif n==3:
        with open('student.txt','r') as f:
            for line in f:
                student=eval(line)
                print(student)
    elif n==4:
        exit()
