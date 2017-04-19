''' 07. Criar um algoritmo que leia um número que será o limite superior de um
intervalo e o incremento (inc). Imprimir todos os números naturais no intervalo
de zero até o limite superior. Suponha que o incremento é maior do que
zero e o limite superior maior que o incremento.'''

def Valor(lim, inc):

    for i in range(0, lim):
        if inc > 0 and lim > inc:
            print(i)

Valor(3, 2)
