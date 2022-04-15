"""
tenho 10 numeros sequências, ex [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fazer o quadrado do número

Syntax of List reverse()
"""

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for numero in numeros:
#     print(f'| {numero} x {numero} |  {numero * numero}  |')

print('\n'.join([f'{numero} x {numero} {numero * numero}' \
    for numero in numeros[::-1]]))

""" desafio extra faça um list_comprehesion da lista de escola colocando 
'E.E.PROF' ['milton', 'camilo', 'don jose', 'don pedro']
E.E.PROF milton
E.E.PROF camilo
E.E.PROF don jose
E.E.PROF don pedro
"""

"""
spread operations
arr = [3, 4, 5]
extended_arr = [1, 2, *arr]
"""