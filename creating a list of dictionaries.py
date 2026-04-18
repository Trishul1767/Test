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


student_list=[]
def add_student(student_list):
    student={}
    student['name']=input("Enter the name of the student: ")
    student['roll']=int(input("Enter the roll number of the student: "))
    student['marks']=float(input("Enter the marks of the student: "))
    student_list.append(student)
print(student_list)

student_list={}
def display_students(student_list):
    for student in student_list:
        print(student)

display_students(student_list)

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

def read_from_file():
    with open('students.txt','r') as f:
        for line in f:
            student=eval(line)
            print(student)
read_from_file()


def find_topper(student_list):
    if not student_list:
        print("No students in the list.")
        return
    max1=student_list[0]
    for student in student_list:
        if student['marks']>max1['marks']:
            max1=student
                    
    print("Topper Information:")
    print(f"Name: {max1['name']}")
    print(f"Roll Number: {max1['roll']}")
    print(f"Marks: {max1['marks']}")
    print(f"Semester: {max1['semister']}")
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
        print("Invalid choice. Please try again.")

