# Somatória de elementos com tratamento para exceções

import os

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print ('Somatória dos elementos 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n')

soma_dos_elementos = input('Pressione "Enter" para exibir o resultado\n')

soma_dos_elementos = 0

try:
    for numero in lista_de_numeros:
        soma_dos_elementos += numero
except Exception as e:
    print(f'Ocorreu um erro: {e}')
    os.system('cls')

print (f'A soma de todos os elementos da lista é: {soma_dos_elementos}\n')

#Resultado "Ok!"