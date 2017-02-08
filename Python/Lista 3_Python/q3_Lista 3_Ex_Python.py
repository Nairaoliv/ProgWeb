#3. Faça uma função que recebe dois números por parâmetro e retorna o maior.


def Funcao(n1, n2):
    maior = 0
    
    if n1 > n2:
        maior = n1
    elif n1 < n2:
        maior = n2

    return "Maior: " + maior
    
    

num1 = input("Numero 1: ")
num2 = input("Numero 2: ")
    

print(Funcao(num1, num2))


