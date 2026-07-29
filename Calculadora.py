def Calcular(operacao, num1, num2):
    if operacao == '+':
        return num1 + num2

    elif operacao == '-':
        return num1 - num2

    elif operacao == '*':
        return num1 * num2

    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"

    elif operacao == '%':
        return num1 % num2

    else:
        return "Operação inválida"