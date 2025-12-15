# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:45:22 2025

@author: jared
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplX = num1 * num2

if num2 != 0:
    divsX = num1 / num2
    print("Division result from the first numbert:",  divsX)
else:
    print("WARNING: Division BY 0 NOT allowed please try again.")

print("Multiplication result:", multiplX)

