# Plano Cartesiano

print ('=== Coordenadas Cartesianas ===\n')

# Solicitação das coordenadas
x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

# Quadrante
if x > 0 and y > 0:
    print('O ponto está no primeiro quadrante')
elif x < 0 and y > 0:
    print('O ponto está no segundo quadrante')
elif x < 0 and y < 0:
    print('O ponto está no terceiro quadrante')
elif x > 0 and y < 0:
    print('O ponto está no quarto quadrante')
else:
    print('O ponto está localizado no eixo ou origem')

    # Resultado "Ok!"