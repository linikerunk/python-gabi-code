""" O que é uma lista
lista - python  === array JavaScript === array PHP === array
"""

# comidas = ['lasanha', 'feijoada', 'strogonoff', 'yakisoba'] # lista

# # """
# # lasanha
# # feijoada
# # strongonoff
# # yakisoba
# # """

# for comida in comidas:
#      print(comida)

list_comprehension = [comida.lower() for comida in [
    'Lasanha',
    'Feijoada',
    'Strogonoff',
    'Yakisoba'
    ]
] 
print(list_comprehension)
