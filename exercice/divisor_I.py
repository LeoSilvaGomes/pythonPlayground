numero = int(input())
i = 1

while i != numero + 1:
    if numero % i == 0:
        print(i)
    i += 1 