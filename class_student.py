from class_person import Person

class Student(Person):
    status = "not working"
    def __init__(self, name, age, school_name, student_id):
        super().__init__(name, age)

        self.school_name = school_name
        self.student_id = student_id

    def show_details(self):
        print(f"My name {self.name}, I'm from {self.school_name}, My id is: {self.student_id}")


print(Student.status)
