# A very simple Python program

print("=== Simple Adder Program ===")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a + b
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers!")
