#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This will contain some stupid functions for the main to call"""


def f1(n1, n2): 
    # this sums 2 numbers, n1 and n2 are integers
    res = n1 + n2
    return res


def ask_numbers(): 
    n1 = int(input("Give me a positive number (bigger than 0): "))

    while n1 < 0: 
        n1 = int(input("Give me a positive number (bigger than 0): "))
    
    n2 = int(input("Give me a number: "))

    return n1,n2
