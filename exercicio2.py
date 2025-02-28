'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada
juntamente com a hora atual.
Exemplo:
Entre 0 - 11: Bom dia
Entre 12 - 17: Boa tarde
Entre 18 - 23: Boa noite
'''

nome = str(input('Olá, qual é o seu nome? '))
hora = int(input(f'{nome}, que horas são por favor? '))

if hora in [0, 11]:
    print(f'Bom dia {nome}!')

elif hora in [12, 17]:
    print(f'Boa tarde {nome}!')

elif hora in [18, 23]:
    print(f'Boa noite {nome}!')