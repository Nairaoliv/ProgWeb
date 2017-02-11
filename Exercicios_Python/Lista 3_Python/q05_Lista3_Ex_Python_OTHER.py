def numParImpar(n):
    if(n % 2 == 0):
        return "Numero par"
    else:
        return "Numero impar"

num = int(input("Digite um numero: "))

print(numParImpar(num))


