sequence = 1
divisor = 1
result = 0

while divisor != 101:
    result += sequence / divisor
    divisor += 1

print(format(result, '.2f'))