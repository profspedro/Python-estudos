frase = 'Curso em vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:12])
print(frase[12:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))

frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Curso')) #indica que a palavra "Curso" está na posição 0
print(frase.find('vídeo')) #indica a posição da palavra "vídeo"
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][2])

print("""A série “O que há de novo no Python” é uma série de ensaios que nos guia através das 
mudanças mais importantes entre as principais versões do Python. 
Ela é imprescindível para aqueles que desejam manter-se atualizados a cada novo lançamento.""")