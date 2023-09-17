# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:45:44 2023

@author: talha.i
"""

# BMI Calculator Part 2

height = float(input('Enter your height in m: '))

weight = float(input('Enter your weight in kg: '))

# Calculations:
bmi = round(weight/(height ** 2), 2)


# IF-ELSE Conditions:
if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are overweight')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese')
else:
    print(f'Your BMI is {bmi}, you are clinically obese')
    