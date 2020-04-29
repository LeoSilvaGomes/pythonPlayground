loop = int(input())

while loop != 0:
    number = int(input())
    i = 0
    result = 0
    while i < number:
        i += 1
        if number % i == 0 and i != number:
            result += i
    if result == number:
        print(str(number) + " eh perfeito")
    else:
        print(str(number) + " nao eh perfeito") 
    loop -= 1