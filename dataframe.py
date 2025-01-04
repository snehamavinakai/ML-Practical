import pandas as pd

# Initialize an empty DataFrame to store student details
columns = ['Student ID', 'Name', 'Age', 'Course', 'Marks']
students_df = pd.DataFrame(columns=columns)

def display_students():
    print("\nStudent Details:")
    print(students_df)

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Student Course: ")
    marks = float(input("Enter Student Marks: "))
    
    # Add the new student to the DataFrame
    new_student = pd.DataFrame([[student_id, name, age, course, marks]], columns=columns)
    global students_df  # You don't need to use this anymore.
    students_df = pd.concat([students_df, new_student], ignore_index=True)
    print("Student added successfully!")

def update_student():
    student_id = input("Enter Student ID to update: ")
    
    # Find the student by ID
    if student_id in students_df['Student ID'].values:
        print("Which detail would you like to update?")
        print("1. Name")
        print("2. Age")
        print("3. Course")
        print("4. Marks")
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            new_name = input("Enter new Name: ")
            students_df.loc[students_df['Student ID'] == student_id, 'Name'] = new_name
        elif choice == 2:
            new_age = int(input("Enter new Age: "))
            students_df.loc[students_df['Student ID'] == student_id, 'Age'] = new_age
        elif choice == 3:
            new_course = input("Enter new Course: ")
            students_df.loc[students_df['Student ID'] == student_id, 'Course'] = new_course
        elif choice == 4:
            new_marks = float(input("Enter new Marks: "))
            students_df.loc[students_df['Student ID'] == student_id, 'Marks'] = new_marks
        else:
            print("Invalid choice!")
            return
        print(f"Student {student_id} updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    
    # Find the student by ID
    if student_id in students_df['Student ID'].values:
        students_df = students_df[students_df['Student ID'] != student_id]
        print(f"Student with ID {student_id} deleted successfully!")
    else:
        print("Student not found.")

def main():
    while True:
        print("\nStudent Details Management System")
        print("1. Display Student Details")
        print("2. Add New Student")
        print("3. Update Student Details")
        print("4. Delete Student Record")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            display_students()
        elif choice == 2:
            add_student()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
