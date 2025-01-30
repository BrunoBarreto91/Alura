# Somatório de números ímpares entre 1 e 10

print ('Somatório dos números ímpares da primeira dezena\n')

sum_of_odds = input('Pressione "Enter" para exibir o resultado\n')

sum_of_odds = 0

for number in range(1,11):
    if number % 2 != 0:
        sum_of_odds +=number

print (f'A soma dos números ímpares de 1 a 10 é: {sum_of_odds}')
print()

# Resultado "Ok!"