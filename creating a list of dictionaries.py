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
3. Write a function called display_students(student_list).

The function should:
a) Traverse through the list of dictionaries
b) Display each student record

student_list={}
def display_students(student_list):
    for student in student_list:
        print(student)

display_students(student_list)

4. Write a function called save_to_file(student_list). 
The function should:
a) Store all student records into a file named students.txt.

def save_to_file(student_list):
    with open('students.txt','w') as f:
        for student in student_list:
            f.write(str(student)+'\n')
student_list=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['roll']=int(input("Enter the roll number of the student: "))
    student['marks']=float(input("Enter the marks of the student: "))
    student['semister']=input("Enter the semester of the student: ")
    student_list.append(student)
save_to_file(student_list)
print(student_list)
with open('students.txt','r') as f:
    print(f.read())

5. Write a function called read_from_file().

The function should:
a) Read the contents of students.txt
b) Display all student records stored in the file.

def read_from_file():
    with open('students.txt','r') as f:
        for line in f:
            student=eval(line)
            print(student)
read_from_file()

6.Write a function called find_topper(student_list).

The function should:
a)Identify the student with the highest marks
b)Display the topper information.'''

def find_topper(student_list):
    if not student_list:
        print("No students in the list.")
        return
    max=student_list[0]['marks']
    for student in student_list:
        if student['marks']>max:
            max=student['marks']
                    
    print("Topper Information:")
    print(f"Name: {max['name']}")
    print(f"Roll Number: {max['roll']}")
    print(f"Marks: {max['marks']}")
    print(f"Semester: {max['semister']}")
student_list=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['roll']=int(input("Enter the roll number of the student: "))
    student['marks']=float(input("Enter the marks of the student: "))
    student['semister']=input("Enter the semester of the student: ")
    student_list.append(student)
find_topper(student_list)
'''
7. Write a menu-driven Python program that repeatedly displays the following options:

a) Add Student
b) Display Students
c) Save to File
d) Read from File
e)Find Topper
f) Exit
The program should continue executing until the user selects Exit.

def display_students(student_list):
    for student in student_list:
        print(student)
def save_to_file(student_list):
    with open('students.txt','w') as f:
        for student in student_list:
            f.write(str(student)+'\n')
def read_from_file():
    with open('students.txt','r') as f:
        for line in f:
            student=eval(line)
            print(student)
def find_topper(student_list):
    if not student_list:
        print("No students in the list.")
        return
    topper = student_list[0]
    for student in student_list:
        if student['marks'] > topper['marks']:
            topper = student
    print("Topper Information:")
    print(f"Name: {topper['name']}")
    print(f"Roll Number: {topper['roll']}")
    print(f"Marks: {topper['marks']}")
    print(f"Semester: {topper['semister']}")

while True:
    print("Menu:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save to File")
    print("4. Read from File")
    print("5. Find Topper")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_list=[]
        n=int(input("Enter the number of students: "))
        for i in range(n):
            student={}
            student['name']=input("Enter the name of the student: ")
            student['roll']=int(input("Enter the roll number of the student: "))
            student['marks']=float(input("Enter the marks of the student: "))
            student['semister']=input("Enter the semester of the student: ")
            student_list.append(student)
    elif choice == 2:
        display_students(student_list)
    elif choice == 3:
        save_to_file(student_list)
    elif choice == 4:
        read_from_file()
    elif choice == 5:
        find_topper(student_list)
    elif choice == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")'''

