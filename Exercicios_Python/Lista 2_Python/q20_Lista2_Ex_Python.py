'''
20. Um algoritmo para realizar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o número de notas
de cada valor que deve ser disponibilizado para o cliente que realizou o saque. Um possível critério seria o da "distribuição
ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo,
se a máquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo
deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que
receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.
'''
def DistribuicaoOtima(valor):
    quociente50 = valor // 50
    quociente10 = (valor % 50) // 10
    quociente5 = (valor % 10) // 5
    quociente1 = (valor % 5) // 1
    

    return str(quociente50) + " notas de R$ 50 \n" + str(quociente10) + " notas de R$ 10 \n" + str(quociente5) + " notas de R$ 5\n" + str(quociente1) + " notas de R$ 1"

valor = int(input("DIGITE UM VALOR: ")) 

print(DistribuicaoOtima(valor))
