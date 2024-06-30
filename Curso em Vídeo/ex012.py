pre = float(input('Qual o preço do produto? '))
des = pre*5/100
npre = pre - des
print('O valor, que custava R$ {}, teve um desconto de 5%, isto é, de R$ {}, e assim o novo preço é igual a R$ {}'.format(pre, des, npre))
