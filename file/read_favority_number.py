from favority_number import *
import json

def open_favority_number():
    '''Try read the filename that has the favority number'''
    filename = 'favority_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def show_favority_number():
    '''Show the favority number'''

    favority_number = open_favority_number()
    if favority_number:
        print('Não precisa dizer, seu numero favorito é ' + favority_number)
    else:
        write_number()
        print('Eu sei seu número favorito! É ' + favority_number)

show_favority_number()