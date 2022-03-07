# 1 - Leia a lista de linguagens de programação
list_linguagem = ["Python", "C++", "C#", "JavaScript", "Java"]

for index, languagem in enumerate(list_linguagem):
    print(f'número : {index} linguaguem : {languagem}')

# 2- Dado uma lista de nomes, associe cada nome 
# com a devida posição de telefone, 0+0, 1+1, 2+2, 3+3 

names = ['Gabrieli', 'Matheus', 'João', 'Marcia']
telefones = [
    '(11) 99850-4231',
    '(11) 99655-4101',
    '(12) 98811-4231',
    '(11) 99551-4030'
]

for name in names:
    for telefone in telefones:
        print(f'nome: {name} e telefone : {telefone}')

for index, name in enumerate(names):
    print('nome:', names[index], 'telefone:', telefones[index])
    print(f'nome: {names[index]} telefone {telefones[index]}')
    print('telefone: {0}, nome : {1}'.format(
        telefones[index],
        names[index])
    )

"""
names = ['Gabrieli', 'Matheus', 'João', 'Marcia']

telefones = [
    '(11) 99850-4231', #Matheus
    '(11) 99655-4101', #Marcia
    '(12) 98811-4231', #João
    '(11) 99551-4030' #Gabrieli
]

resultado = dict("nome : ", valor do telefone : " ") 
"""