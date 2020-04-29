numero = 0
resultado = 0
i = 0

while numero >= 0:
    numero = int(input())
    if numero >= 0:
        resultado = numero + resultado
        i += 1

print(format(resultado/i, '.2f'))