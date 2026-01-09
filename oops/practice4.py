# Find the number is even or odd

class NumberCheck:
    # def __init__(self, number):
    #     self.number = number

    @staticmethod
    def check(num):
        if num % 2 == 0:
            print("even number")
        else:
            print("odd number")

num1 = NumberCheck()
num1.check(5)