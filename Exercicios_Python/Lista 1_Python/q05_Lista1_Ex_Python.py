
horaNormal = float(input("Digite a quantidade de horas trabalhadas : "))
horaExtra = float(input(" Digite a quantidade de horas extras : "))

salBruto = (horaNormal *10) + (horaExtra*15)
salLiquido = salBruto - (salBruto*0.1)

print("Salario bruto.........: ", salBruto)
print("Salario liquido.......: ", salLiquido) 
