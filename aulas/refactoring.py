"""
    A importa da refatoração em um código.
"""


def push_obj(obj, place):
    return f'O {obj} está no lugar {place}'

def test_push_obj():
    obj = 'Sapato'
    place = 'Televisão'

    result = push_obj(obj, place)
    expected_result = "O Sapato está no lugar Televisão"
    
    print(result)
    print(expected_result)
    
    assert result == expected_result

test_push_obj()



"""
    example: refactoring 1
"""

class MinhaFuncao():
    
    def __init__(self, string):
        if string in ['batata', 'morango', 'coca_cola']:
           return getattr(self, string)()
        raise ValueError('Invalid string')

    def batata(self):
        return 'a string é batata'

    def morango(self):
        return 'a string é morango'
        
    def coca_cola(self):
        return 'a string é coca-cola'

MinhaFuncao('qweqweqwe')