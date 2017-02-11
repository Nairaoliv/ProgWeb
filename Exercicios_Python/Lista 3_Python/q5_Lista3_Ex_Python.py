# Crie uma função que recebe um número por parâmetro e retorna o valor booleano verdadeiro se o número
#for par.

def numPar(n):
    return n % 2 == 0

def numImpar(n):
    return not numPar(n)


print(numPar(2))
print(numImpar(2))
print(numPar(3))
print(numImpar(3))
