from PySimpleGUI import PySimpleGUI as sg
import Calculadora as Cal

# LAYOUT DA CALCULADORA

sg.theme('Reddit')
Layout = [
    [sg.Text('Digite o SINAL da OPERAÇÃO desejada :'),sg.Input(key = ('Operacao'), size=(50,5))],
    [sg.Text('Digite seu 1° Valor desejado : '),sg.Input(key =('num1'),size = (50,5))],
    [sg.Text('Digite seu 2° Valor desejado : '),sg.Input(key = ('num2'), size = (50,5))],
    [sg.Button('Calcular')],
    [sg.Text('Resultado: '),sg.Input(key = ('resultado'),size = (50,5))]
]

# Janela

Janela = sg.Window('CALCULADORA',Layout)
while True:
    eventos , valores = Janela.read()

    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Calcular':
        try:
            op = valores['Operacao']
            n1 = float(valores['num1'])
            n2 = float(valores['num2'])

            resultado  = Cal.Calcular(op,n1,n2)

            Janela['resultado'].update(resultado)

        except ValueError:
            Janela['resultado'].update('Digite números válidos!')
Janela.close()