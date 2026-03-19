#creating a list of dictionaries to store information of different students by taking 
student_list=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['roll']=int(input("Enter the roll number of the student: "))
    student['marks']=float(input("Enter the marks of the student: "))
    student['semister']=input("Enter the semester of the student: ")
    student_list.append(student)
print(student_list)

#2.

student_list=[]
def add_student(student_list):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['roll']=int(input("Enter the roll number of the student: "))
    student['marks']=float(input("Enter the marks of the student: "))
    student_list.append(student)
print(student_list)

#3.
'''3. Write a function called display_students(student_list).

The function should:
a) Traverse through the list of dictionaries
b) Display each student record'''

student_list={}
def display_students(student_list):
    for student in student_list:
        print(student)

display_students(student_list)

