class Course:
    def __init__(self, course_id, name, description, price):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.price = price
        self.students = []
        self.quizzes = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} enrolled in {self.name}.")

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)
        print(f"Quiz '{quiz.title}' added to {self.name}.")

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Assignment '{assignment.title}' added to {self.name}.")

    def display_course_details(self):
        print(f"\nCourse ID: {self.course_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price}")
        print(f"Enrolled Students: {len(self.students)}")
        print(f"Quizzes: {[quiz.title for quiz in self.quizzes]}")
        print(f"Assignments: {[assignment.title for assignment in self.assignments]}")


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses_enrolled = []
        self.progress = {}

    def enroll_in_course(self, course):
        self.courses_enrolled.append(course)
        course.add_student(self)
        self.progress[course.course_id] = {"quizzes_completed": [], "assignments_completed": []}
        print(f"{self.name} enrolled in {course.name}.")

    def complete_quiz(self, course, quiz):
        if course.course_id in self.progress:
            self.progress[course.course_id]["quizzes_completed"].append(quiz.title)
            print(f"{self.name} completed quiz '{quiz.title}' in {course.name}.")

    def complete_assignment(self, course, assignment):
        if course.course_id in self.progress:
            self.progress[course.course_id]["assignments_completed"].append(assignment.title)
            print(f"{self.name} completed assignment '{assignment.title}' in {course.name}.")

    def display_progress(self):
        print(f"\nProgress for {self.name}:")
        for course_id, progress in self.progress.items():
            print(f"Course ID: {course_id}")
            print(f"Quizzes Completed: {progress['quizzes_completed']}")
            print(f"Assignments Completed: {progress['assignments_completed']}")


class Quiz:
    def __init__(self, quiz_id, title, questions):
        self.quiz_id = quiz_id
        self.title = title
        self.questions = questions


class Assignment:
    def __init__(self, assignment_id, title, description):
        self.assignment_id = assignment_id
        self.title = title
        self.description = description


class Certificate:
    def __init__(self, certificate_id, student, course):
        self.certificate_id = certificate_id
        self.student = student
        self.course = course

    def generate_certificate(self):
        print(f"\n🎓 Certificate of Completion 🎓")
        print("=============================")
        print(f"This certifies that {self.student.name} has successfully completed the course '{self.course.name}'.")
        print(f"Certificate ID: {self.certificate_id}")
        print("=============================")


class OnlineLearningPlatform:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course '{course.name}' added to the platform.")

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added to the platform.")

    def display_all_courses(self):
        print("\nAvailable Courses:")
        for course in self.courses:
            print(f"{course.course_id}: {course.name} - ${course.price}")

    def display_all_students(self):
        print("\nRegistered Students:")
        for student in self.students:
            print(f"{student.student_id}: {student.name} ({student.email})")

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


def main():
    platform = OnlineLearningPlatform()

    while True:
        print("\n=== Online Learning Platform ===")
        print("1. Add Course")
        print("2. Add Student")
        print("3. Enroll Student in Course")
        print("4. Add Quiz to Course")
        print("5. Add Assignment to Course")
        print("6. Complete Quiz")
        print("7. Complete Assignment")
        print("8. Display Student Progress")
        print("9. Generate Certificate")
        print("10. Display All Courses")
        print("11. Display All Students")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            course_id = int(input("Enter Course ID: "))
            name = input("Enter Course Name: ")
            description = input("Enter Course Description: ")
            price = float(input("Enter Course Price: "))
            course = Course(course_id, name, description, price)
            platform.add_course(course)

        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            student = Student(student_id, name, email)
            platform.add_student(student)

        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            student = platform.find_student_by_id(student_id)
            course = platform.find_course_by_id(course_id)
            if student and course:
                student.enroll_in_course(course)
            else:
                print("Invalid Student ID or Course ID.")

        elif choice == "4":
            course_id = int(input("Enter Course ID: "))
            quiz_id = int(input("Enter Quiz ID: "))
            title = input("Enter Quiz Title: ")
            questions = input("Enter Quiz Questions (comma-separated): ").split(",")
            quiz = Quiz(quiz_id, title, questions)
            course = platform.find_course_by_id(course_id)
            if course:
                course.add_quiz(quiz)
            else:
                print("Invalid Course ID.")

        elif choice == "5":
            course_id = int(input("Enter Course ID: "))
            assignment_id = int(input("Enter Assignment ID: "))
            title = input("Enter Assignment Title: ")
            description = input("Enter Assignment Description: ")
            assignment = Assignment(assignment_id, title, description)
            course = platform.find_course_by_id(course_id)
            if course:
                course.add_assignment(assignment)
            else:
                print("Invalid Course ID.")

        elif choice == "6":
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            quiz_title = input("Enter Quiz Title: ")
            student = platform.find_student_by_id(student_id)
            course = platform.find_course_by_id(course_id)
            if student and course:
                quiz = next((q for q in course.quizzes if q.title == quiz_title), None)
                if quiz:
                    student.complete_quiz(course, quiz)
                else:
                    print("Quiz not found.")
            else:
                print("Invalid Student ID or Course ID.")

        elif choice == "7":
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            assignment_title = input("Enter Assignment Title: ")
            student = platform.find_student_by_id(student_id)
            course = platform.find_course_by_id(course_id)
            if student and course:
                assignment = next((a for a in course.assignments if a.title == assignment_title), None)
                if assignment:
                    student.complete_assignment(course, assignment)
                else:
                    print("Assignment not found.")
            else:
                print("Invalid Student ID or Course ID.")

        elif choice == "8":
            student_id = int(input("Enter Student ID: "))
            student = platform.find_student_by_id(student_id)
            if student:
                student.display_progress()
            else:
                print("Invalid Student ID.")

        elif choice == "9":
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            certificate_id = int(input("Enter Certificate ID: "))
            student = platform.find_student_by_id(student_id)
            course = platform.find_course_by_id(course_id)
            if student and course:
                certificate = Certificate(certificate_id, student, course)
                certificate.generate_certificate()
            else:
                print("Invalid Student ID or Course ID.")

        elif choice == "10":
            platform.display_all_courses()

        elif choice == "11":
            platform.display_all_students()

        elif choice == "12":
            print("Exiting the platform. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()