x = int(input("Enter number1: "))
y = int(input("Enter number2: "))

try:
    z = x / y
except ZeroDivisionError as e:
    print("Division by zero exception:", e)
    z = None
except Exception as e:
    print("Exception type:", type(e).__name__)
    z = None

print("Division is:", z)
