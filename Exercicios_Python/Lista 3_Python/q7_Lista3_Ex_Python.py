'''
7. Crie uma função que recebe o nome e o sexo de uma pessoa, e retorne a mensagem “Ilmo Sr.”, caso seja
informado o sexo masculino, ou “Ilma Sra.”, caso seja informado o sexo feminino. Retorne junto com cada
mensagem de saudação o nome que foi informado.
'''

def RecebeNomeSexo(nome, sexo):
    
    if sexo == "M":
        return "Ilmo Sr. " + nome
    elif sexo == "F":
        return "Ilma Sra. " + nome
    else:
        return "Invalido"

nome = str(input("NOME: "))
sexo = input("SEXO: ")

print(RecebeNomeSexo(nome, sexo))
