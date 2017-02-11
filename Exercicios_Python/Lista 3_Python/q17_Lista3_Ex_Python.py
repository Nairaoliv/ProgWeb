'''
17. A partir de dois números fornecidos pelo usuário, escreva uma das seguintes mensagens:
Os dois são pares
Os dois são impares
O primeiro é par e o segundo é ímpar
O primeiro é ímpar e o segundo é par
'''

def RetornaMensagem(n1, n2):
    if (n1 % 2 == 0) and (n2 % 2 == 0):
        return "Os dois são pares"
    elif (n1 % 2 != 0) and (n2 % 2 != 0):
        return "Os dois são impares"
    elif (n1 % 2 == 0) and (n2 % 2 != 0):
        return "O primeiro é par e o segundo é ímpar"
    elif (n1 % 2 != 0) and (n2 % 2 == 0):
        return "O primeiro é ímpar e o segundo é par"
    
n1 = int(input("NUMERO 1: "))
n2 = int(input("NUMERO 2: "))

print(RetornaMensagem(n1, n2))
