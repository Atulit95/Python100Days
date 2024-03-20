# Adding the art which displays at the start of the program
import art_module

def add(n1, n2):
  """Add two numbers."""
  return format(n1+n2, ".1f")
 
def subtract(n1, n2):
  """Calculates difference between two numbers."""
  return format(n1-n2, ".1f")
 
def multiply(n1, n2):
  """Multiplies two numbers"""
  return format(n1*n2, ".1f")
 
def divide(n1, n2):
  """Provides dividion result with 1 decimal point precision"""
  return  format(n1/n2, ".1f")
operations={
   "+": add,
   "-":subtract,
   "*":multiply,
   "/":divide
   }
def calculator():
    print(art_module.calculator_img())  #Display the image of calculator in program
    first_number=float(input("What's the first number: "))
    print("+\n-\n*\n/")
    continue_calculating="y"
    while continue_calculating=="y":
        operation_symbol=input("Pick an operation?: ")
        if operation_symbol not in operations:
            print("Enter a valid operation.")
            continue
        else:
            second_number=float(input("what's the next number: "))
            calulation_function=operations[operation_symbol]
            result=calulation_function(first_number,second_number)
#............Another way to use line 38 and 39.Repalce them with below to code to check..........................
            # if operation=="+":
            #     result= add(first_number,second_number)
            # elif operation=='-':
            #     result= subtract(first_number,second_number)
            # elif operation=="*":
            #     result= multiply(first_number,second_number)
            # elif operation=="/":
            #     result=divide(first_number,second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {result}")
        first_number=float(result)
        continue_calculating=input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start new calculation: ")
        if continue_calculating=="n":
           print(end="\033c")   # clear the screen for new calculation
           calculator()
calculator()

