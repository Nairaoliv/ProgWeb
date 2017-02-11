#13. Recebe o ano de nascimento de uma pessoa e escreva na tela a sua idade em 31/12/2013.

def RecebeAno(ano):
    idade = ano - 2013

    return "IDADE ATUAL: " + str(idade)


anoNasc = int(input("DIGITE O ANO DE NASCIMENTO: "))
              
print(RecebeAno(anoNasc))
