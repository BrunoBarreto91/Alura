import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]


def exibir_nome_do_programa():
    print("""𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n
""")

def exibir_opcoes():         
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurantes')
    print ('3. Ativar Restaurante')
    print ('4. Sair\n')

def finalizar_app():
    exibir_subtitulo ('Finalizando o App')

def voltar_ao_menu_principal():
    input('\nDigite "Enter" para retornar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

# função "match"
#def escolher_opcao():
#    opcao_escolhida = int(input('Escolha uma opção: '))
#    match opcao_escolhida:
#        case 1:
#            print('Adcionar restaurante')
#        case 2:
#            print('Listar restaurantes')
#        case 3:
#            print('Ativar restaurante')
#        case 4:
#            print('Finalizar app')
#        case _:
#            print('Opção inválida!')

def cadastrar_novo_restaurante():
    exibir_subtitulo ('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome de um restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo ('Listando os restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {'ativo' if ativo else 'inativo'}')

    voltar_ao_menu_principal()

# funções if, else...
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            print('Finalizando o app')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()          