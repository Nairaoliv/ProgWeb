'''
10. João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas
(C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. Como as contas estão
atrasadas, João terá de pagar multa de 2% sobre cada conta.
Faça um algoritmo que calcule e mostre quanto restará do salário do João
'''

def ContaAtrasada(salario, c1, c2):

    multa =  salario - ((c1 * 0.02) + (c2 * 0.02))

    return "Restará do salario de João: " + str(multa)

print(ContaAtrasada(1200, 200, 120))
