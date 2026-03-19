#creating a list of dictionaries to store information of different students by taking 
'''student_list=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['roll']=int(input("Enter the roll number of the student: "))
    student['marks']=float(input("Enter the marks of the student: "))
    student['semister']=input("Enter the semester of the student: ")
    student_list.append(student)
print(student_list)

2. Write a function called add_student(student_list).

The function should:
a) Ask the user to enter student name.
b) Ask the user to enter roll number.
c) Ask the user to enter marks.
d) Store the entered details in a dictionary.
e) Append the dictionary to the student_list.'''
student_list=[]
def add_student(student_list):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['roll']=int(input("Enter the roll number of the student: "))
    student['marks']=float(input("Enter the marks of the student: "))
    student_list.append(student)
print(add_student(student_list))
print(student_list)

