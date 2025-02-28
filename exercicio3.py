'''
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; 
Se tiver 5 ou 6 letras, escreva "seu nome tem um tamanho normal";
Se for maior que 6, "Seu nome é grande".
'''

nome = str(input('Digite seu primeiro nome: '))
if len(nome) <= 4:
    print('Seu nome é curto.')

elif len(nome) in [5, 6]: # verificamos se o tamanho do nome é 5 ou 6
    print('Seu nome tem um tamanho normal.')

else:
    print('Seu nome é grande.')