def TesteIf(L1, L2, L3):
    letras = '';
    if L1 == 'V':
        letras = letras + 'A'
    else:
        if L2 == 'V':
            if L3 == 'V':
                letras = letras + 'B'
            else:
                letras = letras + 'C'
                letras = letras + 'D'
    letras = letras + 'E'
    return letras

#Deve ser digitado apenas V ou F para leitura dos valores

La = input("Digite uma letra: ")
Lb = input("Digite uma letra: ")
Lc = input("Digite uma letra: ")

print(TesteIf(La, Lb, Lc))

#a)Se forem lidos V, V e F, o que será impresso?
#AE

#b) Se forem lidos F, V e F, o que será impresso?
#CDE

#c) Se forem lidos F, V e V, o que será impresso?
#BE

#d) Que valores devem ser lidos para ser escrito apenas a letra ‘E’?
#Todos os valores devem ser Falsos(F)
