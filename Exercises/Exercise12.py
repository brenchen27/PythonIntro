class Student:

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    def getEmail(self):
        email = self.first + "." + self.last + "@" + self.domain
        return email

    def compareGrade(self, anotherStudent):
        if self.grade > anotherStudent.grade:
            print(self.first + " grade is greater than " + anotherStudent.first)
        elif self.grade < anotherStudent.grade:
            print(self.first + " grade is less than " + anotherStudent.first)
        else:
            print(self.first + " grade is the same as " + anotherStudent.first)

student1 = Student("Brendan","Chen","95")
student2 = Student("Chris","Lin","8")

student1.compareGrade(student2)
