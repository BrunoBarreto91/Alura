# Verificação de Chaves

dados_pessoais = [{'nome':'Bruno', 'idade':'33', 'cidade':'São Paulo', 'ativo':True}]

verificar_chave = 'nome'

if verificar_chave in dados_pessoais[0]:
    print(f'A chave {verificar_chave} existe no dicionário.')
else:
    print(f'A chave {verificar_chave} não existe no dicionário.')