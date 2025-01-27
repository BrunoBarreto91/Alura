#Login

print ('=== Autenticação ===\n')

# Valores esperados
usuario_esperado = 'Bruno'
senha_esperada = '1423'

# Solicitação do login
usuario = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

# Validação
if usuario == usuario_esperado and senha == senha_esperada:
    print ('Login efetuado com sucesso!')
else:
    print ('Dados inválidos!')

    # Resultado "Ok!"