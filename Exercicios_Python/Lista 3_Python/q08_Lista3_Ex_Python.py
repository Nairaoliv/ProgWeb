'''
8. Crie uma função que recebe um número inteiro e retorne a mensagem positivo, negativo ou igual a zero, de
acordo com o valor recebido.
'''

def Mensagem(numero):
    if numero > 0:
        return "\nPositivo\n"
    if numero < 0:
        return "\nNegativo\n"
    else:
        return "\nIgual a zero\n"

numero = int(input("DIGITE UM NUMERO: "))

print(Mensagem(numero))
