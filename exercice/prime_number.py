import math

loop = int(input())

for i in range(0, loop):
    number = int(input())
    count = 0
    for l in range(1, int(math.pow(number, 1/2)) + 1):
        if number % l == 0: 
            count += 1
        if count > 1:
            break
    if count == 1:
        print(str(number) + " eh primo")
    else:
        print(str(number) + " nao eh primo")