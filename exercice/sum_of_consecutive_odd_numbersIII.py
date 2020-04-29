loop = int(input())

while loop != 0:
    result = 0
    x, y = map(int, input().split())
    if x % 2 == 0:
        x += 1
        while y != 0:
            result += x
            x += 2
            y -= 1
    else:
        while y != 0:
            result += x
            x += 2
            y -= 1
    loop -= 1
    print(result)