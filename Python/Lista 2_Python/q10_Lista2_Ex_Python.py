#10. Escreva um algoritmo/programa que mostre o triplo de um número informados pelo usuário.

def RecebeNum(n):
    valor = n * 3
    return "TRIPLO: " + str(valor)

num = int(input("DIGITE UM NUMERO: "))
print(RecebeNum(num))
