'''09. Criar um algoritmo que leia um número (n) e imprima a soma dos números
múltiplos de 5 no intervalo aberto entre 1 e num.
Suponha que n será maior que 1.'''

def SomaMultiploCinco(num):
    soma = 0
    for i in range(1, num+1):
        if i%5 == 0 and i > 1:
            soma = soma + i

    print("Soma dos Multiplos de 5 = ", soma)
            

num = int(input("INSIRA UM NUMERO (intervalo): "))

SomaMultiploCinco(num)
