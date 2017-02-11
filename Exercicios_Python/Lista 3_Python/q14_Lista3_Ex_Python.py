'''
14. Crie uma função que recebe o ano de nascimento de uma pessoa e retorna uma mensagem que diga se ela
poderá ou não votar em uma eleição para prefeito, não é necessário considerar o mês ou o dia que ela nasceu.
'''

from datetime import datetime
now = datetime.now()

def RetornaVotacao(anoNasc):
    if (now.year - anoNasc > 18):
        return "\nVocê pode votar nas eleições para Prefeito."
    else:
        return "\nVocê NÃO pode votar nas eleições para Prefeito."

anoNasc = int(input("DIGITE O ANO EM QUE VOCÊ NASCEU: "))
print(RetornaVotacao(anoNasc))
