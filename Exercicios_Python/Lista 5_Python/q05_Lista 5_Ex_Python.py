'''5. Leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.'''

def Consoantes():
    C = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

    
    for i in C:
        if i == "a" or "e" or "i" or "o":
            print(i)

Consoantes()
