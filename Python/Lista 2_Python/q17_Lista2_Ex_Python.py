'''
17. Em época de pouco dinheiro os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Recebe o valor de
um produto e o percentual de desconto concedido e imprima o valor do produto com desconto.
'''

def RecebeDesconto(valor, perc):
    desconto = valor * (perc/100)
    total = valor - desconto
    return "VALOR TOTAL COM DESCONTO: " + str(total)


valor = int(input("DIGITE UM VALOR: "))
perc = int(input("DIGITE O PERCENTUAL DO DESCONTO: "))

print(RecebeDesconto(valor, perc))
