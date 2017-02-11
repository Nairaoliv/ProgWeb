#12. Recebe quatro números e imprima a média ponderada, sabendo-se que os pesos são respectivamente 1, 2, 3 e 4.

def MediaPonderada(n1, n2, n3, n4):
    media = (n1*1 + n2*2 + n3*3 + n4*4) / (1 + 2 + 3 + 4)
    return  "MEDIA PONDERADA: " + str(media)


num1 = int(input("NUMERO 1: "))
num2 = int(input("NUMERO 2: "))
num3 = int(input("NUMERO 3: "))
num4 = int(input("NUMERO 4: "))

print(MediaPonderada(num1, num2, num3, num4))
