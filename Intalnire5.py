# def print_hi(user):
#     print(f'Salut{user}')
#     print('Salut')
#
#
# print_hi('Madalina')


# calculam impozitul pe masina
cc = input('Introduceti capacitatea cilindrica') # se introduce capacitatea cilindrica a masinii
impozit = None


def calcul_impozit(hibrid_input, cc_input):
    if hibrid_input == True:
        return 10
    elif cc_input < 1200:
        return 75
    elif cc_input < 1600:
        return 125
    elif cc_input < 2500:
        return 200
    else:
        return 500


impozit = calcul_impozit(False, cc)
print(impozit) # 75
impozit = calcul_impozit(False, 1199)
print(impozit) # 100
impozit = calcul_impozit(False, 1599)
print(impozit)  # 125
impozit = calcul_impozit(False, 1999)
print(impozit) # 200

