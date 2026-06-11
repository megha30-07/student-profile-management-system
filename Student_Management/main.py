import sqlite3
from database import connect

connect()

def add_student():
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")
        marks = float(input("Enter Marks: "))

        cursor.execute("INSERT INTO students (name, age, department, marks) VALUES (?, ?, ?, ?)",
                       (name, age, dept, marks))

        conn.commit()
        conn.close()
        print("Student added successfully!")

    except ValueError:
        print("Invalid input!")


def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def update_student():
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        student_id = int(input("Enter ID to update: "))
        new_marks = float(input("Enter new marks: "))

        cursor.execute("UPDATE students SET marks=? WHERE id=?", (new_marks, student_id))

        conn.commit()
        conn.close()
        print("Updated successfully!")

    except:
        print("Error updating data!")


def delete_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()
    print("Deleted successfully!")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice")