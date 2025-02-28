'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''

while True: # criamos um loop infinito, e somente será quebrado, se o usuário digitar um número válido.
    try: # se caso o usuário digite um número, o código entra no try, que realizará o script de validação
        numero = int(input('Digite um número inteiro qualquer: '))

        if numero:

            if numero % 2 == 0: # verificando se o número é par ou não
                print(f'O número {numero} é par.')
            else:
                print(f'O número {numero} é ímpar.')

            break # o loop infinito só será quebrado quando o usuário responder corretamente o input

    except ValueError: # capturamos o erro ValueError, caso o usuário digite algo que não seja o que queremos, por exemplo abc ou 1,2 ou 3.5 etc.
        print('Entrada inválida! Por favor, digite um número inteiro válido.')

    




