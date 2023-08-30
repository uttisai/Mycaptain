class Student:
    def __init__(self, student_id, first_name, last_name, age):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.student_id}: {self.first_name} {self.last_name}, Age: {self.age}"


def add_student():
    student_id = input("Enter Student ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    age = input("Enter Age: ")

    student = Student(student_id, first_name, last_name, age)

    with open("student_records.txt", "a") as file:
        file.write(f"{student.student_id},{student.first_name},{student.last_name},{student.age}\n")

    print("Student added successfully!")


def main():
    while True:
        print("\nSchool Administration Program")
        print("1. Add Student")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()

