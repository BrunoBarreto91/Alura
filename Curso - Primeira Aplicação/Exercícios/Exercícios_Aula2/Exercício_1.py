#número par ou impar

print ('Número par ou impar!\n')

def par_ou_impar(numero):
    return 'par' if numero % 2 == 0 else 'ímpar'

numero = int(input('Digite um número:'))
print(f'{numero} é {par_ou_impar(numero)}.')

#resultado "ok!"