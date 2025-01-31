# Contagem de frequência de palavras na frase

import string

frequencia = {}

def frequencia_de_palavras(frase):
    palavras = frase.split()

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia

frase = 'Para aprender a aprender, é preciso praticar a prática constantemente.'

freq_de_palavras = frequencia_de_palavras(frase)

print(freq_de_palavras)


