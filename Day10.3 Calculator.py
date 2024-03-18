# Adding the art which displays at the start of the program
import calculator_art

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  """Multiplies two numbers"""
  return n1 * n2
 
def divide(n1, n2):
  return  format(n1/n2, ".1f")
restart="y"
while restart=="y":
    print(calculator_art.img())
    first_number=float(input("What's the first number: "))
    print("+\n-\n*\n/")
    continue_calculating="y"
    while continue_calculating=="y":
        operation=input("Pick an operation?: ")
        if not (operation == "+" or operation =="-" or operation =="*" or operation =="/"):
            print("Enter a valid operation.")
            continue
        else:
            second_number=float(input("what's the next number: "))
            if operation=="+":
                result= add(first_number,second_number)
            elif operation=='-':
                result= subtract(first_number,second_number)
            elif operation=="*":
                result= multiply(first_number,second_number)
            elif operation=="/":
                result=divide(first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        first_number=result
        continue_calculating=input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start new calculation: ")
        if continue_calculating=="n":
           restart="y"
           print(end="\033c")


