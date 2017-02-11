#11. Recebe nome, endereço e telefone e imprima na tela.

def Funcao(n, e, t):

    return "\nNome: " + n + "\nEndereco: " + e + "\nTelefone: " + str(t)


nome = str(input("NOME COMPLETO: "))
endereco = str(input("ENDERECO: "))
telefone =  int(input("TELEFONE: "))

print(Funcao(nome, endereco, telefone))
