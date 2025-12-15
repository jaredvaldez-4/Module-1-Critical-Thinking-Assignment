# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:45:22 2025

@author: jared
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    print("Division result from the first numbert:", division)
else:
    print("Division by zero is not allowed please try again.")

print("Multiplication result:", multiplication)
