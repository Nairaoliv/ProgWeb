'''
12. Escreva uma função que recebe um número inteiro e retorna a mensagem “O número é múltiplo de 7” ou “O
número não é múltiplo de 7”.
'''

def RetornaMultiplo(valor):
    if(valor % 7 == 0):
        return "\nO número é múltiplo de 7\n"
    else:
        return "\nO número não é múltiplo de 7\n"

valor = int(input("DIGITE UM VALOR: "))
print(RetornaMultiplo(valor))
