'''
19. Escreva uma função que recebe a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e
retorne a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.
'''

def SinalTransito(cor):

        if (cor == 'V'):
            return "\nSiga"
        elif (cor == 'A'):
            return "\nAtencao"
        elif (cor == 'E'):
            return "\nPare"
        else:
            return "\nInvalido"



cor = str(input("DIGITE A COR DO SINAL (V, A, ou E): "))

print(SinalTransito(cor.upper()))



    
