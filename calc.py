'''
    Program: Magic Calculator: Udemy course
    Author: Vishrut Jha
    Cpoyright: 2018-19
'''

import re

print ("PyCalc: My first calculator on Python")
print ("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    # if there has been a previous calculation, use that result as prompt
    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))
    
    # if user quits ->
    if equation == 'quit':
        run = False
        print("Goodbye, Human!")
    else:
        equation = re.sub('[a-zA-Z,:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()