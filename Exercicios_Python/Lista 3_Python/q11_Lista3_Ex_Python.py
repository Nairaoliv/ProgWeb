'''
11. Crie uma função que recebe a temperatura de uma pessoa e retorna “Está com febre” ou “Sem febre”.
Considere o valor base como 36.5.
'''

def RetornaTemperatura(temperatura):
    if temperatura > 36.5:
        return "Está com febre"
    else:
        return "Sem febre"

temperatura = float(input("DIGITE A TEMPERATURA: "))
print(RetornaTemperatura(temperatura))
