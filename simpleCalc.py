#simple Calculator
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operation=input("Enter a mathematical operation of your choice (+,-,*,/): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
print(num1, operation, num2, "=", result)
