number = 1
while number != 0:
    number = int(input())
    if number == 0:
        break
    result = 0
    i = 0
    if number % 2 == 0:
        while i != 5: 
            result += number
            i += 1
            number += 2
    else: 
        number += 1
        while i != 5: 
            result += number
            i += 1
            number += 2
    print(result)    