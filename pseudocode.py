from random import randint
from math import pi
from datetime import date

def CHAR():
    alphabet = list('bcdfghijamesklnopqrtuvwxyz')
    char = alphabet[randint(0, 25)]
    return char


def INTEGER():
    integer = randint(0, 1000000000000)
    if integer != "0":
        neg = randint(0, 1)
        if neg == 1:
            integer = integer - (2 * integer)
            return integer
        else:
            return integer
    else:
        return integer

def REAL():
    real = (float(randint(0, 1000000000000)))/pi
    if real != "0":
        neg = randint(0, 1)
        if neg == 1:
            real = real - (2 * real)
            return real
        else:
            return real
    else:
        return real

def STRING():
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    alphabetlist = list(alphabet)
    strlen = randint(0, 25)
    string = ''
    for x in range(0, strlen):
        string = string + alphabetlist[randint(0, 25)]
    return string

def BOOLEAN():
    query = input('ask a true or false question: ')
    if query == 'should you check the problem solving website every night':
        boolean = 'TRUE'
        return boolean
    boolean = ['TRUE', 'FALSE']
    return boolean[randint(0, 1)]

def DATE():
    evenmonths = ['2', '4', '6', '8', '10', '12']
    year = randint(1, 5000)
    month = randint(1, 12)
    if month == 2:
        leap = randint(1, 4)
        if leap == 1:
            day = randint(1, 29)
    else:
        day = randint(1, 31)
        if day == 31 and month in evenmonths:
            day == day - 1
    return date(year, month, day)
