# Palavras reservadas do python
# exercio 1
""" cadastro de uma escola, onde vc terá professores e alunos
cada professor terá nome, email, materia_lecionada, salario, e alunos terá nome e materia"""

""" DESAFIO PARA O PESSOAL DA AULA GABI-CODE : """
escola = {
    'nome': 'Escola do Sol',
    'professores': [],
    'alunos': []
}

professor = {
    'nome': 'Ricardao',
    'email': 'ricardao@gmail.com',
    'materia_leciona': 'Física Quântica',
    'salario': 15.000
}

aluno = {
    'nome': 'Guilherme TV',
    'materia': 'Física Quântica'
}

escola['professores'].append(professor)
escola['alunos'].append(aluno)


print(f"escola : {escola['nome']}")
print(f"professor : {professor['nome']}")
print(f"email : {professor['email']}")
print(f"materia_leciona : {professor['materia_leciona']}")
print(f"salario : {professor['salario']:.3f}")
print(f"aluno : {aluno['nome']}")
print(f"materia do aluno : {aluno['materia']}")
