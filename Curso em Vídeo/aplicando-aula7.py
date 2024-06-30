nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
soma = n1 + n2
prod = n1 * n2
div = n1 / n2
divi = n1 // n2
exp = n1 ** n2
print('A soma é {}, \no produto é {} e a\n divisão é {:.2f}. '.format(soma, prod, div), end='')
print('Divisão inteira {} e potência {}'.format(divi, exp))

