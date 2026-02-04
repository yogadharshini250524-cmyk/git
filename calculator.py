first_number=int(input("Enter the first number: "))
operator=input("pick an operator (+, -, *, /): ")
second_number=int(input("Enter the second number: "))
def calculator(first, operator, second):
    if operator == "+":
        result = first + second
        print(f"{first} + {second} = {result}")
    elif operator == "-":
        result = first - second
        print(f"{first} - {second} = {result}")
    elif operator == "*":
        result = first * second
        print(f"{first} * {second} = {result}")
    elif operator == "/":
        if second != 0:
            result = first / second
            print(f"{first} / {second} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator. Please pick one of (+, -, *, /).")
option=input("Do you want to continue? (yes/no): ")
if option.lower() == "yes":
    calculator(first=first_number, operator=operator, second=second_number)
else:
    print("Goodbye!")
