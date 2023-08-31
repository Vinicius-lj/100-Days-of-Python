from art import logo
from os import system

def add(num1, num2):  
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

operators = {"+":add,"-":sub,"*":mult,"/":div,}
while True:
  print(logo)
  number1 = int(input("Whats the first nuumber? "))
  loop = True
  while loop:
    print("+\n-\n*\n/")
    operator = input("Pick a operation: ")
    number2 = int(input("Whats the next number? "))
    result = operators[operator](number1, number2)
    print(f"{number1} {operator} {number2} = {result} ")
    new_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if new_calc == "n":
      loop = False
    number1 = result
  system("cls")
