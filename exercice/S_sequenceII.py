sequence = 1
divisor = 1
result = 0

while sequence != 39:
    result += sequence / divisor
    divisor += divisor
    sequence += 2

print(format(result, '.2f'))