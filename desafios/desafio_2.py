from datetime import datetime as dt

""" Exercio 2: Fazer um programa para ler a duracao de tempo em segundos,
dai imprimir na tela esta duração no formato horas:minutos:segundos.

"""

seconds = input("Digite o valor em segundos : ")
""" existe um regra aqui para converter o second em Date()"""
time_converted = dt.strftime("%H:%M:%S") # strftime -> converte a string em 
# data passando os parametros H como hora, M como minutos, %S como segundos.
print(segundos)
