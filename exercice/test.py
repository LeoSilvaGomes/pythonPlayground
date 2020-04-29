numero1 = 1
numero2 = 1
while numero1 != 0 or numero2 != 0:
    numero1, numero2 = map(int, input().split())
    if numero1 == 0 or numero2 == 0:
        break
    if numero1 > 0:
        if numero2 > 0:
            print("primeiro")
        else:
            print("quarto")
    else:
        if numero2 > 0:
            print("segundo")
        else:
            print("terceiro")