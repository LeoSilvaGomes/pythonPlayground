import json

def write_number():
    '''Write on file the favority number'''
    number = input("Tell me your favority number: ")
    
    filename = 'favority_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)