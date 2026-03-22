# 2. Write a function called add_student(student_list)
def add_student(student_list):
    student = {}
    student['name'] = input("Enter the name of the student: ")
    student['roll_no'] = int(input("Enter the roll number of the student: "))
    student['marks'] = float(input("Enter the marks of the student: "))
    student['semester'] = input("Enter the semester of the student: ")
    
    student_list.append(student)
    print("Student added successfully!")

# 3. Write a function called display_students(student_list)
def display_students(student_list):
    if not student_list:
        print("No students to display.")
        return
    for student in student_list:
        print(student)

# 4. Write a function called save_to_file(student_list)
def save_to_file(student_list):
    with open('students.txt', 'w') as f:
        for student in student_list:
            f.write(str(student) + '\n')
    print("Data saved to file successfully!")

# 5. Write a function called read_from_file()
def read_from_file():
    try:
        with open('students.txt', 'r') as f:
            print("Student records from file:")
            for line in f:
                student = eval(line.strip())
                print(student)
    except FileNotFoundError:
        # This prevents an error if you press '4' before pressing '3'
        print("File not found! Please save data to the file first.")

# 6. Write a function called find_topper(student_list)
def find_topper(student_list):
    if not student_list:
        print("No students in the list.")
        return
    
    topper = student_list[0]
    for student in student_list:
        if student['marks'] > topper['marks']:
            topper = student
            
    print("\nTopper Information:")
    print(f"Name: {topper['name']}")
    print(f"Roll Number: {topper['roll_no']}")
    print(f"Marks: {topper['marks']}")
    print(f"Semester: {topper['semester']}")

# 1. Create an empty list called student_list
# We define this ONCE before the loop starts so it doesn't get erased!
student_list = []

# 7. Write a menu-driven Python program
while True:
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save to File")
    print("4. Read from File")
    print("5. Find Topper")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Notice how much cleaner this is when we just call the function!
        add_student(student_list) 
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