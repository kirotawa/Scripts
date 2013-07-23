# -*- coding: utf-8 -*-

__author__ = 'Leônidas S. Barbosa (kirotawa)'
__email__ = 'kirotawa@gmail.com'


def dectobin(number):
    bin = ""
    while (number >= 1):
        n_aux = number / 2
        bin += str(number - (n_aux * 2))
        number = n_aux
    print "binary:", bin[::-1]


if __name__ == "__main__":
    dectobin(input("decimal:"))
