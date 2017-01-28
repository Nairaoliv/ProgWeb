<<<<<<< HEAD
"----------------------Questao 1-------------------------"
soma, sub, mult, divisao = float, float, float, float

def Calculo(num1, num2):
    
    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    divisao = num1 / num2

    print("Soma = ", soma, "Subtracao = ", sub, "Multiplicacao = ", mult, "Divisao = ", divisao)  

def questao1():
    n1 = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))

    Calculo(n1, n2)

"----------------------Questao 2-------------------------"
prestacoes = float

def Compra(valor):
    prestacoes = valor / 5
    print("Prestacoes: ", prestacoes)

def questao2():
    valorCompra = float(input("Valor da compra: "))

    Compra(valorCompra)
    
"----------------------Questao 3-------------------------"
preco, percent, valor = float, float, float


def Calculo(preco, percent):
    venda = float
    
    venda = percent/100
    valor = (venda * preco) + venda
    print("Valor: ", valor)

   
def questao3():
    
    nome = input ("Nome do Produto: ")
    p1 = float(input("Preco de custo R$: "))
    p2 = float(input("Porcentual de ganho: "))
    
    Calculo(p1, p2)
"----------------------------------------------------------"

def Main():
    n = int
    while n != 0:
        n = int(input("Numero da questao: "))
        if n == 1:
            questao1()
        elif n == 2:
            questao2()
        elif n == 3:
            questao3()
        elif n == 0:
            print("Opcao Invalida")

Main()
=======
"----------------------Questao 1-------------------------"
soma, sub, mult, divisao = float, float, float, float

def Calculo(num1, num2):
    
    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    divisao = num1 / num2

    print("Soma = ", soma, "Subtracao = ", sub, "Multiplicacao = ", mult, "Divisao = ", divisao)  

def questao1():
    n1 = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))

    Calculo(n1, n2)

"----------------------Questao 2-------------------------"
prestacoes = float

def Compra(valor):
    prestacoes = valor / 5
    print("Prestacoes: ", prestacoes)

def questao2():
    valorCompra = float(input("Valor da compra: "))

    Compra(valorCompra)
    
"----------------------Questao 3-------------------------"
preco, percent, valor = float, float, float


def Calculo(preco, percent):
    venda = float
    
    venda = percent/100
    valor = (venda * preco) + venda
    print("Valor: ", valor)

   
def questao3():
    
    nome = input ("Nome do Produto: ")
    p1 = float(input("Preco de custo R$: "))
    p2 = float(input("Porcentual de ganho: "))
    
    Calculo(p1, p2)
"----------------------------------------------------------"

def Main():
    n = int
    while n != 0:
        n = int(input("Numero da questao: "))
        if n == 1:
            questao1()
        elif n == 2:
            questao2()
        elif n == 3:
            questao3()
        elif n == 0:
            print("Opcao Invalida")

Main()
>>>>>>> 67fd57a4d1283b9bc97d91128d3e7ed4bb6e3b3b
