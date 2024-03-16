'''class calc:
    def __init__(self):
        pass
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        if y==0:
            return "Error : Division by 0!!"
        else:
            return x/y

calc= calc()
def try_again():
    choice=input("do you wanna try again??(yes/no): ")
    return choice.lower()=='yes'
while True:
    
    num1=float(input("enter first number:"))
    num2=float(input("enter the second number:"))
    operation=input("enter the operation(+,-,*,/):")

    if operation== '+':
        result=calc.add(num1,num2)
    elif operation== '-':
        result=calc.sub(num1,num2)
    elif operation== '*':
        result=calc.mul(num1,num2)
    elif operation== '/':
        result=calc.div(num1,num2)
    else:
        result="invalid operation"

    print("result:",result)
    if not try_again():
        break'''

class Calculator:
    def _init_(self):
        pass

    def calculate(self, expression):
        operators = set('+-*/')
        # Split the expression into operands and operators
        parts = expression.split()
        # Check if the expression has the correct format
        if len(parts) % 2 == 0 or any(char not in operators and not char.isdigit() for char in expression):
            return "Invalid expression!"
        
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return "Error: " + str(e)

# Create an instance of the Calculator class
calc = Calculator()

# Function to check if the user wants to try again
def try_again():
    choice = input("Do you want to try again? (yes/no): ")
    return choice.lower() == 'yes'

# Main loop to perform calculations
while True:
    # Take user input for the mathematical expression
    expression = input("Enter a mathematical expression (e.g., 5 + 3, 10 * 2, etc.): ")

    # Perform the calculation
    result = calc.calculate(expression)
    print("Result:", result)

    # Ask if the user wants to try again
    if not try_again():
        print("goodbye")
        break
