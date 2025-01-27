import os

def exibir_nome_do_programa():
    print("""𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n
""")

def exibir_opcoes():         
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurantes')
    print ('3. Ativar Restaurante')
    print ('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o App\n')

# função "match"
def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Adcionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        case _:
            print('Opção inválida!')


# funções "if,else..."
#   if opcao_escolhida == 1:
#           print('Cadastrar restaurante')
#    elif opcao_escolhida == 2:
#            print('Listar restaurante')
#    elif opcao_escolhida == 3:
#            print('Ativar restaurante')
#    else:
#        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()          