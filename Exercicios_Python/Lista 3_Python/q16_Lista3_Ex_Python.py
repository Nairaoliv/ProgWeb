'''
16. Crie uma função que recebe um número inteiro e retorne qual mês do ano o mesmo corresponde. Se o valor
for maior que doze ou menos que um, diga que o valor não corresponde a nenhum mês.
'''

def RetornaMes(numero):
    mes = ["Janeiro", "Fevereiro", "Março", "Abril","Maio",
           "Junho", "Julho", "Agosto", "Setembro",
           "Outubro", "Novembro", "Dezembro"]

    if (numero >= 1) and (numero <= 12):
        resultado = mes[numero-1]
        return resultado
    else:
        return "Valor não corresponde a nenhum mês"
    
    

numero = int(input("DIGITE UM NUMERO: "))
print(RetornaMes(numero))
