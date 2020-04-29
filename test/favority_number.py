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