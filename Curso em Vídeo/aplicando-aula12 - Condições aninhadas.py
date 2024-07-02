nome = str(input('Qual é seu nome? '))
if nome == 'Pedro':
    print('Que nome bonito! ! !')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Tiago':
    print('Seu nome é popular no Brasil.')
elif nome in 'Priscila Paula Tavares':
    print('Belo nome feminino')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}!'.format(nome))
