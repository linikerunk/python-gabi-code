"""
Aula Extra

"""
LIGHT_SPEED = 300.000000

class Calculator():
    number_left = ''
    number_right = ''

    def set_number_left(self, number_left):
        self.number_left = number_left
    
    def set_number_right(self, number_right):
        self.number_right = number_right
    
    def custom_sum(self):
        return  float(self.number_left) - float(self.number_right)

calculator = Calculator()
calculator.set_number_left(18)
calculator.set_number_right(5)
print(calculator.custom_sum())