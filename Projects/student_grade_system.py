while True:
    num_students = int(input("How many students? (press 0 to exit): "))

    if num_students == 0:
        print("Exiting program ...")
        break

    total_marks = 0

    for i in range(1, num_students + 1):
        marks = float(input(f'Enter marks for student {i}: '))
        total_marks += marks

    average = total_marks / num_students
    print(f'Class Average : {average:.2f}')
