numeros = [value**3 for value in range(1, 11)]

print(str(numeros) + '\n')

for numero in numeros[:3]:
    print('Os 3 primeiros numeros são ' + str(numero))

print('\n')

for numero in numeros[4:7]:
    print('Os 3 numeros do meio são ' + str(numero))

for numero in numeros[-3:]:
    print('Os 3 ultimos numeros da fila são ' + str(numero))