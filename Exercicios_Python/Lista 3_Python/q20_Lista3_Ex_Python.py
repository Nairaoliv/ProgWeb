'''
20. O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso
ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa
está em quilogramas e a altura em metros. Faça uma função que retorna o IMC de uma pessoa, e depois, exiba
uma das seguintes mensagens:
'''

def IMC(peso, altura):
    calculo = peso / (altura**2)

    if calculo < 18.5:
        return "Abaixo do peso"
    elif calculo < 25:
        return "Peso normal"
    elif calculo < 30:
        return "Sobrepeso"
    elif calculo < 35:
        return "Obeso Leve"
    elif calculo < 40:
        return "Obeso moderado"
    elif calculo >= 40:
        return "Obeso mórbido"


peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a altura: "))
print(IMC(peso, altura))
