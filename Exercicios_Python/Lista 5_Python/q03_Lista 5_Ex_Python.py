'''
3. Leia uma lista de 10 números reais e mostre-os na ordem inversa
'''

def Lista(n):
    i = 0
    seq = []

    while i < n:
        num = int(input("Numero: "))
        seq.append(num)
        i += 1
    print("Sequencia original: ", seq)

    seq.reverse()
    print("Sequencia inversa: ", seq)

n = int(input("Quantidade de numeros: "))    
Lista(n)
