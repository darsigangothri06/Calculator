from sys import exit
from time import sleep

def add(operands):
    res = 0
    for i in operands:
        res += i
    result(res)

def subtract(operands):
    res = operands[0]
    for i in range(1,len(operands)):
        res -= operands[i]
    result(res)

def multiply(operands):
    res = 1
    for i in operands:
        res *= i
    result(res)

def divide(operands):
    res = operands[0]
    for i in range(1,len(operands)):
        res /= operands[i]
    result(res)

def remainder(operands):
    res = operands[0]
    for i in range(1,len(operands)):
        res %= operands[i]
    result(res)

def result(res):
    print("Your result is: {}".format(res))
    Ask_for_another_command()

def Ask_for_another_command():
    another_command = input("Do you want to enter another command: (yes = 1/ no = 0): ")
    if another_command == '1':
        Start()
    elif another_command == '0':
        print("---------Thankyou---------")
    else:
        print("Enter valid input")
        Ask_for_another_command()
        
def calculate(operand,operators):
    if operand == "add":
        add(operators)
    elif operand == "subtract":
        subtract(operators)
    elif operand == "multiply":
        multiply(operators)
    elif operand == "divide":
        divide(operators)
    elif operand == "remainder":
        remainder(operators)
    else:
        print("Enter valid command")
        user_instructions()

def validate_input(command):
    inst = command.split()
    operator_command = inst[0]
    operators = inst[1].split(',')
    L = [int(i) for i in operators]
    calculate(operator_command,L)
    
def user_instructions():
    command = input("""
Enter your command as <command><space><operands_separated_by_comma>
Example: add 2,3 and multiply 2,3,8
Possible Commands are: add, multiply, subtract, divide, remainder.

Enter your command here: """)
    validate_input(command)

def Start():
    print()
    print("------------Python Calculator------------")
    print()
    print("""Operations performed are:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulo Division""")
    sleep(1)
    user_instructions()

Start()
