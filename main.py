#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""This is the main function"""
import someFunctions

def main(): 
    n1,n2 = someFunctions.ask_numbers()
    r = someFunctions.f1(n1, n2)
    print("Hey I have a solution! {}".format(r))

if __name__ == "__main__": 
    main()
    