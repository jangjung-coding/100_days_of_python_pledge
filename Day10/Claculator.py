print("Welcome to the Calculator!")

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):    
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():
    should_continue = True 
    num1 = float(input("What is the first number?: "))

    while should_continue:
        operation = input("Pick an operation from the following: +, -, *, /: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\n"*20)
            calculator()
            
calculator()