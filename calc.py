def aplication(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def division(a, b): return a / b
def division_by_integer(a, b): return a // b
def degree(a, b): return a ** b

def select_operation(choice):
    if choice == '+':
        return aplication
    elif choice == '-':
        return subtract
    elif choice == '*':
        return multiply
    elif choice == '/':
        return division
    elif choice == '//':
        return division_by_integer
    elif choice == '**':
        return degree
    
operation = select_operation('-') 
print(operation(int(input(':')), int(input(':'))))