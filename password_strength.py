# -*- coding: utf-8 -*-
import re

def case_sensitivity_test(password):
    if (password.upper() != password) and (password.lower() != password):
        return 2
    return 0

def digits_test(password):
    if re.search('[0-9]', password):
        return 2
    return 0

def special_symbols_test(password):
    if re.search('[@ # \$ ! \. \* \? \/ <  \\ >]', password):
        return 2
    return 0

def correct_password_test(password):
    if re.search('[^ a-zA-Z0-9_@#\$!\.\*\?\/<\\>]', password):
        return False
    return True

def password_length_test(password):
    if len(password) <= 8:
        return 0
    elif len(password) <= 12:
        return int((len(password) + 1 - 8) / 2)
    else:
        return 3

def is_popular_password(password):
    f = open('popular_password.txt')
    for line in f:
        if line == password:
            return True
    return False
    
    
def get_password_strength(password):
    rating = 1
    rating += case_sensitivity_test(password) + digits_test(password) + special_symbols_test(password) + password_length_test(password)
    if (not password_length_test(password)) or is_popular_password(password):
        rating = 1
    return rating
    
    

if __name__ == '__main__':
    while True:
        password = input() 
        if not correct_password_test(password):
            print("Incorrect formart of password, try again")    
        else:
            break
    print("Your rating: ", get_password_strength(password))
