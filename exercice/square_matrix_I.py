import math

number = 1

while number != 0:
    number = int(input())
    half = math.ceil(number/2)
    for i in range(1, number+1):
        printer = 1
        for j in range(1, number + 1):
            if j != number+1:
                print("  ", end='')
            if half == i and j <= half:
                print(j, end='')
            elif i <= half and j == half:
                print(i, end='')
            elif i < half and j < half:
                if i < j:
                    print(i, end='')
                else:
                    print(j, end='') 
            elif i > half and j < half:
                if 1+number-i < j:
                    print(1+number-i, end='')
                else:
                    print(j, end='') 
            elif i > half and j > half:
                if 1+number-i < 1+number-j:
                    print(1+number-i, end='')
                else:
                    print(1+number-j, end='')
            elif i < half and j > half:
                if i < 1+number-j:
                    print(i, end='')
                else:
                    print(1+number-j, end='')          
            elif half == i and j > half:
                print(number-j+1, end='')
            elif i > half and j == half:
                print(number-i+1, end='')
            if j != number:
                print(" ", end='')
        print("")
    if number != 0:
        print("")