#creating a list of dictionaries to store information of different students by taking 
student_list=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['age']=int(input("Enter the age of the student: "))
    student['grade']=input("Enter the grade of the student: ")
    student_list.append(student)
print(student_list)