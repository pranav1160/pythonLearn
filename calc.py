a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operation name: ")

if (op == "+"):
    print("Your sum is", a + b)
elif op == "-":
    print("Your difference is", a - b)
elif op == "*":
    print("Your product is", a * b)  # Corrected multiplication operation
elif op == "%":
    print("Your remainder is", a % b)
else:
    print("Error: Invalid operation")
