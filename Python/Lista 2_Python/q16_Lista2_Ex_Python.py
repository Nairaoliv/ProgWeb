#16. Recebe o valor do lado de um quadrado e imprima a sua área e o seu perímetro.

def areaQuadrado(lado):
    return lado * lado

def perimetroQuadrado(lado):
    return lado * 4

lado = float(input("DIGITE O LADO DO QUADRADO : "))

print(" AREA : %.2f" % areaQuadrado(lado))
print(" PERIMETRO : %.2f" % perimetroQuadrado(lado))
