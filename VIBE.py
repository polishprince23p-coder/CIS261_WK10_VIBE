#Michael Korman
#CIS261
#WK10 VIBE Coding

class Student:
    def __init__(self, name, student_id, test1, test2, test3):
        self.name = name
        self.id = student_id
        self.test_scores = [test1, test2, test3]
        self.average = self.calculate_average()
        self.grade = self.calculate_letter_grade()
        self.grade_points = self.calculate_grade_points()

    def calculate_average(self):
        return sum(self.test_scores) / len(self.test_scores)

    def calculate_letter_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def calculate_grade_points(self):
        grade = self.grade
        grade_points = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0,
        }
        return grade_points.get(grade, 0.0)

    def to_record(self):
        return (
            f"Student Name: {self.name} | Student ID: {self.id} | "
            f"Test 1: {self.test_scores[0]} | Test 2: {self.test_scores[1]} | "
            f"Test 3: {self.test_scores[2]} | Student GPA: {self.average:.2f} | "
            f"Letter Grade: {self.grade} | Grade Points: {self.grade_points}"
        )


def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid numeric score.")


def add_student(students):
    print("\nAdd Student")
    name = input("Enter student name: ").strip()
    while not name:
        print("Student name cannot be empty. Please enter a name.")
        name = input("Enter student name: ").strip()

    student_id = input("Enter student ID: ").strip()
    while not student_id:
        print("Student ID cannot be empty. Please enter an ID.")
        student_id = input("Enter student ID: ").strip()

    if any(student.id == student_id for student in students):
        print(f"A student with ID '{student_id}' already exists. Please use a different ID.")
        return

    test1 = get_valid_score("Enter Test 1 score: ")
    test2 = get_valid_score("Enter Test 2 score: ")
    test3 = get_valid_score("Enter Test 3 score: ")

    student = Student(name, student_id, test1, test2, test3)
    students.append(student)
    print(f"Student '{name}' with ID '{student_id}' was added successfully.")
    print("You can add more students now or choose another option from the menu.")


def display_students(students):
    if not students:
        print("No student records are available right now.")
        return

    print(f"\nAll Student Records ({len(students)} total):")
    for student in students:
        print(student.to_record())


def find_student(students):
    student_id = input("Enter student ID to search: ").strip()
    for student in students:
        if student.id == student_id:
            print(f"Student found for ID '{student_id}':")
            print(student.to_record())
            return
    print(f"No student found with ID '{student_id}'.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            print(f"Student '{student.name}' with ID '{student_id}' was deleted successfully.")
            return
    print(f"No student found with ID '{student_id}' to delete.")


def save_students(students):
    try:
        with open("student_grades.txt", "w") as file:
            for student in students:
                file.write(student.to_record() + "\n")
        print("Student records saved successfully to student_grades.txt.")
    except OSError as exc:
        print(f"Error saving file: {exc}. Please check the file location and permissions.")


def calculate_class_gpa(students):
    if not students:
        print("No student records available to calculate GPA.")
        return

    class_gpa = sum(student.grade_points for student in students) / len(students)
    print(f"Class GPA: {class_gpa:.2f}")


def view_individual_gpa(students):
    student_id = input("Enter student ID to view GPA: ").strip()
    for student in students:
        if student.id == student_id:
            print(
                f"Student GPA for '{student.name}' (ID: {student_id}): "
                f"{student.average:.2f} ({student.grade})"
            )
            return
    print(f"No student found with ID '{student_id}'.")


def main():
    students = []

    print("\nWelcome! You can enter multiple students before choosing option 8 to exit.")

    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Find Student")
        print("4. Delete Student")
        print("5. Save Records")
        print("6. View Class GPA")
        print("7. View Individual GPA")
        print("8. Exit")

        choice = input("Choose an option from 1 to 8: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            save_students(students)
        elif choice == "6":
            calculate_class_gpa(students)
        elif choice == "7":
            view_individual_gpa(students)
        elif choice == "8":
            print("Saving records before exiting...")
            save_students(students)
            print("Program ended. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()

