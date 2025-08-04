def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

while True:
    print("\n--- Simple CLI Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("The Result is :", add(num1, num2))
        elif choice == '2':
            print("The Result is :", subtract(num1, num2))
        elif choice == '3':
            print("The Result is :", multiply(num1, num2))
        elif choice == '4':
            print("The Result is :", divide(num1, num2))
    else:
        print("Invalid choice. Please try again.")