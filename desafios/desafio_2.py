from datetime import datetime, time


""" Exercio 2: Fazer um programa para ler a duracao de tempo em segundos,
dai imprimir na tela esta duração no formato horas:minutos:segundos.
"""

seconds = int(input("Digite o valor em segundos: "))
""" existe um regra aqui para converter o second em Date()"""
if (seconds // 3600) > 23:
    d = (seconds // 3600) // 24
    h = (seconds // 3600) % 24
else:
    d = 0
    h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60
hora1 = str(f'{seconds//3600}:{m}:{s}')
print(f'Formato 1 (horas:minutos:segundos - sem formatação correta, conforme pedido nos exemplos do exercício):\n{hora1}\n') # RESPOSTA MASI CORRETA E IDENTICA À SOLUÇÃO DO EXERCICIO PROPOSTO

print(f'Formato 2 (horas:minutos:segundos - com formatação correta. Se a quantidade de horas exceder 24 ou multiplo de 24, aparecem apenas as horas restantes):\n{time(h,m,s).strftime("%H:%M:%S")}\n') # RESPOSTA COM UMA FORMATAÇÃO MELHOR MAS NÃO ATENDE À TODOS OS EXEMPLOS


# FORMA DE RESULTADO QUE MELHOR ATENDE AO EXERCÍCIO PROPOSTO COM A FORMATAÇÃO OBEDECENDO OS LIMITES DE TEMPO
print('Formato 3 (dias:horas:minutos:segundos):')
if d == 0:
    hora = str(datetime(year=2020, month=9, day=22, hour=h, minute=m, second=s))
    print(f'00:{hora[11:]}')
else:
    hora = str(datetime(year=2020, month=4, day=d, hour=h, minute=m, second=s))
    if d < 10:
        print(f'0{d}:{hora[11:]}')
    else:
        print(f'{d}:{hora[11:]}')

if seconds // 3600 < 24:
    print(f"\nFormato 4 (horas:minutos:segundos - com formatação correta. Se a quantidade de horas exceder 24 não será exibido):\n{str(datetime.strptime(hora1, '%H:%M:%S'))[11:]}")
else:
    print('\nFormato 4 não suportado. Quantidade de horas fora do escopo permitido (0...23).\n')
    
