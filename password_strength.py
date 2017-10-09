import re
import getpass
import string
special_symbols = '@#\$!\.\*\?\/<\\>'


def get_result_of_case_sensitivity_test(password):
    if (password.upper() != password) and (password.lower() != password):
        return 2
    return 0


def get_result_of_digits_test(password):
    if re.search('[' + string.digits + ']', password):
        return 2
    return 0


def get_result_of_special_symbols_test(password):
    if re.search('[' + special_symbols + ']', password):
        return 2
    return 0


def get_result_of_correct_password_test(password):
    return not re.search('[^' + string.ascii_letters +
                         special_symbols + string.digits + ']', password)


def get_result_of_password_length_test(password):
    min_password_length = 8
    required_password_length = 12
    if len(password) <= 8:
        return 0
    elif len(password) <= 12:
        # password rating depends on the length
        return int((len(password) + 1 - min_password_length) / 2)
    else:
        return 3


def get_result_of_popular_password_test(password):
    with open('popular_password.txt', 'r') as file_with_popular_password:
        return password in file_with_popular_password


def get_password_strength(password):
    password_rating = 1
    password_rating += sum([get_result_of_case_sensitivity_test(password),
                           get_result_of_digits_test(password),
                           get_result_of_special_symbols_test(password),
                           get_result_of_password_length_test(password)])
    if (not get_result_of_password_length_test(password) or
            get_result_of_popular_password_test(password)):
        password_rating = 1
    return password_rating


if __name__ == '__main__':
    while True:
        password = getpass.getpass()
        if not get_result_of_correct_password_test(password):
            print("Incorrect format of password, try again")
        else:
            break
    print("Your rating: ",  get_password_strength(password))
