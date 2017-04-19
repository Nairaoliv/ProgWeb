'''
08. Recebe 2 números inteiros, retorne o quociente e o resto da divisão do 1º pelo 2º. Recebe um número inteiro e imprima de
volta na tela.
'''

def RecebeNumInt(n1, n2):
    quociente = int(n1 / n2)
    resto = n1 % n2
    return "QUOCIENTE: " + str(quociente)+ " ; " + " RESTO: " + str(resto)

num1 = int(input("NUMERO 1: "))
num2 = int(input("NUMERO 2: "))

print(RecebeNumInt(num1, num2))
