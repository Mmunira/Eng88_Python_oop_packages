class Simple_calc:

    def add(self, value1, value2):
        return value1 + value2

    def substract(self, value1, value2):
        return value1 - value2

    def divide(self, value1, value2):
        return value1 / value2

    def multiply(self, value1, value2):
        return value1 * value2

calc_object = Simple_calc()

print(calc_object.add(2, 5))