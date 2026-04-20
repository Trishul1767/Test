def calculate_sem2_sgpa():
    # 1. Dictionary mapping Gitam's letter grades to their grade points
    grade_scale = {
        'O': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'C': 5,
        'P': 4,
        'F': 0
    }

    # 2. Dictionary of your specific Semester 2 courses and their exact credits
    # Note: Labs for TP courses are combined into the main subject's credit pool
    my_courses = {
        "Digital Logic Circuits": 2,
        "Programming for Problem Solving - 2": 3,
        "Foundations of EEE": 4,
        "Fundamentals of Entrepreneurship": 2,
        "Communicative English - II": 2,
        "Linear Algebra": 4,
        "Engineering Physics": 4
    }

    total_credit_points = 0
    total_credits = 0

    print("--- Trishul's Semester 2 SGPA Calculator ---")
    print("Enter your expected grade (O, A+, A, B+, B, C, P, F) for each subject:\n")

    # 3. A loop that goes through each course and asks for your input
    for subject, credits in my_courses.items():
        while True:
            # Takes your input, strips extra spaces, and converts it to uppercase
            grade_input = input(f"{subject} ({credits} credits): ").strip().upper()
            
            # 4. Logic gate (if/else) to check if the grade is valid
            if grade_input in grade_scale:
                points = grade_scale[grade_input]
                total_credit_points += (points * credits)
                total_credits += credits
                break # Moves to the next subject
            else:
                print("Invalid input. Please enter a valid Gitam grade (e.g., A+, O, B).")

    # 5. Final calculation
    sgpa = total_credit_points / total_credits
    
    print("\n" + "="*30)
    print("FINAL RESULTS")
    print("="*30)
    print(f"Total Credits: {total_credits}")
    print(f"Total Scored Points: {total_credit_points}")
    print(f"Estimated SGPA: {sgpa:.2f}")

# Calling the function to execute the program
calculate_sem2_sgpa()