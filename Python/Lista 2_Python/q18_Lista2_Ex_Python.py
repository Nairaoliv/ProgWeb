'''
18. Recebe dois valores para as variáveis A e B, efetuar a troca dos valores de forma que a variável A passe a ter o valor de B e
que a variável B passe a ter o valor de A. Mostrar na tela os valores trocados.
'''

def RecebeValorTrocado(a, b):
    aux = a
    a = b
    b = aux
    return "\nInverso: \nVARIAVEL A : " + str(a) + "\nVARIAVEL B : " + str(b) 


a = int(input("VARIAVEL A: "))
b = int(input("VARIAVEL B: "))


print(RecebeValorTrocado(a, b))
