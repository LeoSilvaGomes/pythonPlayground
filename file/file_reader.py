filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    
    birthday = input("Enter your birthday, in the form mmddyy: ")
    if str(birthday) in pi_string:
        print('Your birthday appear in pi')
    else:
        print('Your birthday does not appear in pi')