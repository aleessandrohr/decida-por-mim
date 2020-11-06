from funções import *
from random import randint

respostas = ['Sim', 'Não', 'Não deve', 'Deve', 'Talvez sim', 'Talvez não', 'Seria bom', 'Seria ruim', 'Dane-se', 'Yes', 'No', 'Claro que sim', 'Claro que não', 'Ok']

texto('Decida por mim', color='\033[33m')
while True:
    pergunta = str(input('''O que deseja perguntar para mim?
'''))
    resposta = randint(0, len(respostas)-1)
    if pergunta == '.exit':
        texto('FINALIZADO O PROGAMA', color='\033[31m')
        break
    elif pergunta == '.help':
        print(f'\033[30mDigite .exit para finalizar o progama!\033[m')
    else:
        print(f'{respostas[resposta]}')
