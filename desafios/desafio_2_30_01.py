import datetime

""" Exercio 2: Fazer um programa para ler a duracao de tempo em segundos,
dai imprimir na tela esta duração no formato horas:minutos:segundos.

"""

seconds = input("Digite o valor em segundos : ")
print(datetime.timedelta(seconds=int(seconds))) # strftime -> converte a string em 
