'''
15. Crie uma função que recebe uma letra e retorna “verdadeiro” se for uma vogal.
'''
def RetornaVogal(vogal):

    
    if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
        return "\nVerdadeiro\n"
    else:
        return "\nFalso\n"

vogal = str(input("DIGITE UMA LETRA: "))
print (RetornaVogal(vogal.lower()))
