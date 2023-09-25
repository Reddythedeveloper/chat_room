import logging
import datetime

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        return [student.name for student in self.students]

    def schedule_assignment(self, assignment):
        self.assignments.append(assignment)

    def list_assignments(self):
        return [assignment.details for assignment in self.assignments]

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class Assignment:
    def __init__(self, details, deadline):
        self.details = details
        self.deadline = deadline
        self.submissions = []

    def submit(self, student):
        self.submissions.append(student)

class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}

    def add_classroom(self, name):
        if name in self.classrooms:
            logging.error(f"Classroom '{name}' already exists.")
        else:
            self.classrooms[name] = Classroom(name)
            logging.info(f"Classroom '{name}' has been created.")

    def list_classrooms(self):
        return list(self.classrooms.keys())

    def remove_classroom(self, name):
        if name in self.classrooms:
            del self.classrooms[name]
            logging.info(f"Classroom '{name}' has been removed.")
        else:
            logging.error(f"Classroom '{name}' not found.")

    def add_student(self, student_id, class_name, student_name):
        if class_name in self.classrooms:
            student = Student(student_id, student_name)
            self.classrooms[class_name].add_student(student)
            logging.info(f"Student {student_id} has been enrolled in {class_name}.")
        else:
            logging.error(f"Classroom '{class_name}' not found.")

    def list_students(self, class_name):
        if class_name in self.classrooms:
            return self.classrooms[class_name].list_students()
        else:
            logging.error(f"Classroom '{class_name}' not found.")
            return []

    def schedule_assignment(self, class_name, assignment_details, deadline):
        if class_name in self.classrooms:
            assignment = Assignment(assignment_details, deadline)
            self.classrooms[class_name].schedule_assignment(assignment)
            logging.info(f"Assignment for {class_name} has been scheduled.")
        else:
            logging.error(f"Classroom '{class_name}' not found.")

    def list_assignments(self, class_name):
        if class_name in self.classrooms:
            return self.classrooms[class_name].list_assignments()
        else:
            logging.error(f"Classroom '{class_name}' not found.")
            return []

    def submit_assignment(self, student_id, class_name, assignment_details):
        if class_name in self.classrooms:
            classroom = self.classrooms[class_name]
            student_found = False
            for assignment in classroom.assignments:
                if assignment.details == assignment_details:
                    for student in classroom.students:
                        if student.student_id == student_id:
                            assignment.submit(student)
                            logging.info(f"Assignment submitted by Student {student_id} in {class_name}.")
                            student_found = True
                            break
                    if not student_found:
                        logging.error(f"Student {student_id} is not enrolled in {class_name}.")
                    break
            else:
                logging.error(f"Assignment '{assignment_details}' not found in {class_name}.")
        else:
            logging.error(f"Classroom '{class_name}' not found.")

def main():
    logging.basicConfig(filename='virtual_classroom.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    classroom_manager = VirtualClassroomManager()

    while True:
        print("\nVirtual Classroom Manager")
        print("1. Add Classroom")
        print("2. List Classrooms")
        print("3. Remove Classroom")
        print("4. Add Student")
        print("5. List Students")
        print("6. Schedule Assignment")
        print("7. List Assignments")
        print("8. Submit Assignment")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter classroom name: ")
            classroom_manager.add_classroom(name)
        elif choice == "2":
            classrooms = classroom_manager.list_classrooms()
            print("Classrooms:", classrooms)
        elif choice == "3":
            name = input("Enter classroom name to remove: ")
            classroom_manager.remove_classroom(name)
        elif choice == "4":
            student_id = input("Enter student ID: ")
            class_name = input("Enter classroom name to enroll in: ")
            student_name = input("Enter student name: ")
            classroom_manager.add_student(student_id, class_name, student_name)
        elif choice == "5":
            class_name = input("Enter classroom name to list students: ")
            students = classroom_manager.list_students(class_name)
            print("Students:", students)
        elif choice == "6":
            class_name = input("Enter classroom name to schedule assignment: ")
            assignment_details = input("Enter assignment details: ")
            deadline = input("Enter assignment deadline (YYYY-MM-DD): ")
            classroom_manager.schedule_assignment(class_name, assignment_details, deadline)
        elif choice == "7":
            class_name = input("Enter classroom name to list assignments: ")
            assignments = classroom_manager.list_assignments(class_name)
            print("Assignments:", assignments)
        elif choice == "8":
            student_id = input("Enter student ID: ")
            class_name = input("Enter classroom name: ")
            assignment_details = input("Enter assignment details: ")
            classroom_manager.submit_assignment(student_id, class_name, assignment_details)
        elif choice == "9":
            print("Exiting Virtual Classroom Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
