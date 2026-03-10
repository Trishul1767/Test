def save_student_info(student_name, university):
    # 'with' handles the opening and the automatic closing
    with open("student_profile.txt", "w") as file:
        file.write(f"Name: {student_name}\n")
        file.write(f"University: {university}\n")
        
    print("Information saved successfully!")

# Calling the function
save_student_info("Trishul", "Gitam Hyderabad")
with open("student_profile.txt", "r") as file:
    content = file.read()
    print(content)