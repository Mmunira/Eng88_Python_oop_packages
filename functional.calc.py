
from oop_calc_task import Simple_calc
class Functional_calc:

    def __init__(self):
        super().__init__()
    def conversion(self, num1):
            return num1 * 2.54

    def divisible(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def triangle(self, height, width):
        return height * width / 2

fun_object = Functional_calc()

# create a function for cm to inch
# create a function for divisible by 0, check if the number is divisible by 0 return True else return False

# print statements for all functions available in parent class as well as this child class

