'''
9. Escreva uma função que recebe e retorne o valor booleano “verdadeiro” caso o número seja múltiplo de 5, ou
“falso”, caso contrário.
'''

def RetornaValor(valor):
    
    if (valor % 5 == 0):
        return "\nverdadeiro\n"
    else:
        return "\nfalso\n"
    
valor = int(input("DIGITE UM VALOR: "))
print(RetornaValor(valor))
