
class Student:
    schoolName = "ABC School"

    # def __init__(self):
    #     print("Whenever a new object is created, I am called automatically.")
    #     print(self)

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Sankar","BCA")
print(student1.name)
print(student1.course)