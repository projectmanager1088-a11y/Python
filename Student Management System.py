student = []

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. update Student")
    print("4. View Students")
    print("5. search student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student name: ")
        student_age = input("Enter student age: ")
        student.append([student_name, student_age])

    if choice == "4":
         for s in student:
             print("Student Name:", s[0])
             print("Student Age:", s[1])
    if choice == "5":
        search_name = input("Enter student name to search: :")
        for s in student:
            if search_name == s[0]:
             print("Student Name:", s[0])
             print("Student Age:", s[1])
    if choice == "3":
        update_name = input("Enter student name to update: ")
        for s in student:
             if update_name == s[0]:
                new_name = input("Enter student name: ")
                new_age = input("Enter student age: ")
                s[0]=new_name
                s[1]=new_age

    if choice == "2":
        remove_student = input("Enter student name: ")
        for s in student:
            if remove_student == s[0]:
                student.remove(s)
                print("Student Removed successfully.")
                break
    if choice == "6":
        print("Thank you for using Student Management System")
        break