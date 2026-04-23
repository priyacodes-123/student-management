from model import StudentManager

manager = StudentManager()

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Show Low Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            name = input("Enter Name: ")
            attendance = float(input("Enter Attendance %: "))
            marks = float(input("Enter Marks: "))
            manager.add_student(name, attendance, marks)
            print("Student Added Successfully!")
        except:
            print("Invalid Input!")

    elif choice == "2":
        students = manager.get_students()
        if not students:
            print("No Records Found")
        for name, att, marks in students:
            grade = manager.calculate_grade(marks)
            print(f"Name: {name}, Attendance: {att}%, Marks: {marks}, Grade: {grade}")

    elif choice == "3":
        low = manager.low_attendance()
        if not low:
            print("No students below 75% attendance")
        for s in low:
            print(f"{s[0]} - {s[1]}%")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")