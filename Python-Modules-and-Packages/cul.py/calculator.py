from mymath import add, sub as s
choice = input("What do you want to calculate? (add or sub): ")
if choice == "add":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add(num1, num2)
    print("Result:", result)
elif choice == "sub":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = s(num1, num2)
    print("Result:", result)
else:
    print("Invalid choice! Please enter 'add' or 'sub'.")
