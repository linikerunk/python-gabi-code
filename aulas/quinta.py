"""
Quinta Aula - python recursivo
-------------------------------------------------------------------------------
"""

def factorial(number):
    """
        This is a recursive function
        to find the factorial of an integer
    """
    number_model = number - 1
    
    if number == 1 or number == 0:
        return 1
    return (number * factorial(number_model))

print("The factorial of", 0, "is", factorial(0))