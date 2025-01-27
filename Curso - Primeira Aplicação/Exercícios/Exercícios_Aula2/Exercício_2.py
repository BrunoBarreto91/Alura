#Classificação de idade

print ('-Classificação Etária-\n')

idade = int(input('Informe a idade e saiba qual é a classificação etária: '))

if idade <= 12:
    print ('Criança')
elif 13 <= idade <= 18:
    print ('Adolescente')
else:
    print ('Adulto')

# Resultado "Ok!"