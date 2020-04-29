loop = int(input())

while loop != 0:
    pa, pb, g1, g2 = [float(x) for x in input().split()]
    i = 0
    g1 = g1/100
    g2 = g2/100
    while int(pa) <= int(pb):
        pa += int(pa * g1)
        pb += int(pb * g2)
        i += 1
        if i > 100:
            print("Mais de 1 seculo.")
            break
    if i <= 100:
        print(str(i) + " anos.")
    loop -= 1
