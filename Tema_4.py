
# ex 1
# masini = ['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']

# punctul a
# for masina in range(len(masini)):
#     print(f"Masina mea preferata este {masini[masina]}")
#
#  punctul b
# for masina in masini:
#     print(f"Masina mea preferata este {masina}")

# punctul c
# masina = 0
# while (masina<len(masini)):
#     print(f'Maina mea favorita este {masini[masina]}')
#     masina += 1;



# ex. 2

# prima_masina = masini[0]
# ultima_masina = masini[len(masini) - 1]
# for masina in range(1, len(masini)-1):
#     masini[masina] = masini[masina].upper()
# else:
#     print(masini)

# ex. 3

# for masina in masini:
#     if masina == 'Mercedes':
#         print(f'Am gasit masina dorita de dvs {masina} !')
#         break
#     else:
#         print(f'Am gasit masina {masina}, Mai cautam.')

# Ex. 4

# for masina in masini:
#     if masina == 'Trabant':
#         continue
#     if masina == 'Lastun':
#         continue
#     print(f'S-ar putea sa va placa masina {masina}, o masinade exceptie.')

# ex. 5

# masina_veche = []
# for masina in range(len(masini)):
#     if masini[masina] == 'Trabant':
#         masina_veche.append('Trabant')
#         masini[masina] = 'Tesla'
#     if masini[masina] == 'Lastun':
#         masina_veche.append('Lastun')
#         masini[masina] = 'Tesla'
# print(f'Modelele vechi sunt: {masina_veche}')
# print(f'Modelele noi sunt: {masini}')

# ex. 6

# masina_pret = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# buget_masina = 15000
# for key, value in buget_masina.items():
#     if value <= buget_masina:
#         print(f'Pentru bugetul dvs{buget_masina} euro puteti sa va alegeti {key} fla pretul de {value}.')

# ex. 7

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# numar_norocos = []
# for x in numere:
#     if x == 3:
#         numar_norocos.append(x)
# print(f'Numarul meu norocos 3 apare de {len(numar_norocos)} ori.')

# ex. 8

# x = 0
# for y in numere:
#     x += y
# print(x)

# ex. 9

# for x in numere:
#     x = sorted(numere)[-1]
# print(x)

# Ex. 10

# for x in numere:
#     print(-x)

# Ex. 11

# alt_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# even_numbers = []
# odd_numbers = []
# positive_numbers = []
# negative_numbers = []
# for x in alt_numbers:
#     if x % 2 == 0:
#         even_numbers.append(x)
#     else:
#         odd_numbers.append(x)
#     if x >= 0:
#         positive_numbers.append(x)
#     if x < 0:
#         negative_numbers.append(x)
# print(f'The list with even numbers is {even_numbers}.')
# print(f'The list with odd numbers is {odd_numbers}.')
# print(f'The list with positive numbers is {positive_numbers}.')
# print(f'The list with negative numbers is {negative_numbers}.')

# Ex. 12

# for i in range(len(alt_numbers)):
#     for j in range(0, len(alt_numbers) - i - 1):
#         if alt_numbers[j] > alt_numbers[j + 1]:
#             x = alt_numbers[j]
#             alt_numbers[j] = alt_numbers[j + 1]
#             alt_numbers[j + 1] = x
# print(f'Sorted List in Ascending Order:\n{alt_numbers}')

# Ex. 13

# import random
# secret_number = random.randint(1, 30)
# print(secret_number)
# guess = 1
#
# while guess != secret_number:
#     guess = int(input("Try to guess the number:\n"))
#     if guess > secret_number:
#         print("Wrong! You guessed too high")
#     if guess < secret_number:
#         print("Wrong! You guessed too low")
# else:
#     print("You got it!")

# Ex. 14

# rows = int(input(f'Please insert a number for your pyramid:\n'))
# print(f'Look at the pyramid !')
# for i in range(rows + 1):
#     for j in range(i):
#         print(i, end='')
#     print('')

# Ex. 15

# keyboard_phone = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for x in keyboard_phone:
#     for y in keyboard_phone[1]:
#         print(f'Current digit is {y}')
#     break

