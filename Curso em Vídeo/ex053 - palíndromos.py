'''enunciado: Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços
Exemplos:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA'''
frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
'''inverso = ''
for letra in range (len(junto) - 1,-1,-1):
    inverso += junto[letra]'''
inverso = junto[::-1] #fatiamento
print('O inverso de {} é {}'.format(junto,inverso))
if inverso==junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')

#print(junto,inverso)

#print('Você digitou  frase {}'.format(junto))
