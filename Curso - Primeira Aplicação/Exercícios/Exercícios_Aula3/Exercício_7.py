# Calculo de média com tratamento para divisão por zero

import os

lista_de_numeros = [5,10,20,40,80]

def exibir_nome_do_programa():
    print ('Calculo de média')

def exibir_opcao():
    input('Calculo de média dos elementos 5,10,15,30,60. Pressione "Enter".\n')
    calcular_media()

def Encerrar_programa():
    input('\nDigite "Enter" para fechar')
    os.system('cls')

def calculo_invalido():
    print ('Erro: Não é possível dividir por zero. A lista esta vazia')
    Encerrar_programa()

def calcular_media():
    try:
        average = sum(lista_de_numeros) / len(lista_de_numeros)
    except ZeroDivisionError:
        calculo_invalido()
    else:
        print(f'A média dos valores na lista é: {average}\n')

def main():
    exibir_nome_do_programa()
    exibir_opcao()


if __name__== '__main__':
    main()
