
#Entrada da Operação

Operacao = input('\nDigite o sinal da operação desejada : ')
# Lista - > Passando a operação para a programação

lista = ['+','-','*','/','%']

#Logica para Realizar a Operação
def Calcular():
   if Operacao in lista:
         if Operacao == '+':
            num1 = float(input('\nDigite Primeiro Valor:  '))
            num2 = float(input('\nDigite o Segundo Valor:  '))
            resultado = num1 + num2
            print('O Resultado da Soma é :\n', resultado)

         elif Operacao == '-':
            num1 =float(input('\nDigite o Primeiro Valor:  '))
            num2 = float(input('\nDigite o Segundo Valor:  '))
            resultado = num1 - num2
            print('O Resutado da Subtração é :\n',resultado)

         elif Operacao == '*':
            num1 = float(input('\nDigite o Primeiro Valor:  '))
            num2 = float(input('\nDigite o Segundo Valor:  '))
            resultado = num1 * num2
            print('O Resultado da Multiplicação é:\n', resultado)

         else:
            num1 = float(input('\nDigite o Primeiro Valor:  '))
            num2 = float(input('\nDigite o Segundo Valor:  '))
            resultado = num1 / num2
            print('O Resultado da Divisão é:\n', resultado)
   else:
      print('Operação inválida!')

Calcular()