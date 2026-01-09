# Create a class Student that takes 3 marks and has a method average().

class Student:
    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list

    def average(self):
        print("Hello,", self.name)
        add = 0
        for mark in self.marks_list:
            add += mark

        print("Average is: ", add/len(self.marks_list))

student1 = Student("Sankar",[99,91,99])
student1.average()