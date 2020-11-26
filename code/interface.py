from PySimpleGUI import *
from random import randint


respostas = ['Sim', 'Não', 'Não deve', 'Deve', 'Talvez sim', 'Talvez não', 'Seria bom', 'Seria ruim', 'Dane-se', 'Yes', 'No', 'Claro que sim', 'Claro que não', 'Ok']

change_look_and_feel('Default1')

layout = [
    [Text('O que deseja perguntar para mim?')],
    [Input(size=(30,0), key='dados')],
    [Button('Perguntar'), Button('Sair')],
    [Output(size=(30,10))]
]

janela = Window('Decida por mim').layout(layout)

while True:
    event, values = janela.Read()
    try:
        pergunta = str(values['dados'])
    except:
        print('-' * 52)
        print('Verifique os dados e\ntente novamente.')
        print('-' * 52)
    else:
        if pergunta == '':
            print('-' * 52)
            print('Verifique os dados e\ntente novamente.')
            print('-' * 52)
        else:
            resposta = randint(0, len(respostas)-1)
            print('-' * 52)
            print(f'{respostas[resposta]}')
            print('-' * 52)
    if event == WIN_CLOSED or event == 'Sair':
        break

janela.close()

