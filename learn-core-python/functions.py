# ---------------------------------------------------
# Program 1: Calculate Total Expenses Using a Function
# This program defines a function that takes a list
# of expenses and returns the total sum.
# The same function is reused for different people.
# ---------------------------------------------------

def calculate_sum(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


vishal_exp_list = [2111, 3411, 3511]
veera_exp_list = [20, 30, 40]

vishal_total = calculate_sum(vishal_exp_list)
veera_total = calculate_sum(veera_exp_list)

print("Vishal's total expenses:", vishal_total)
print("Veera's total expenses:", veera_total)


# ---------------------------------------------------
# Program 2: Understanding Local vs Global Variables
# This program shows that a variable created inside
# a function is LOCAL to that function and does not
# affect the variable outside the function.
# ---------------------------------------------------

total = 0

def sum(a, b):
    print("a:", a)
    print("b:", b)
    total = a + b   # This 'total' is a LOCAL variable
    print("Total inside function:", total)
    return total


n = sum(b=2, a=3)
print("Total outside the function:", total)


# ---------------------------------------------------
# Program 3: Function with Default Argument
# This function takes two integer arguments.
# The second argument 'b' has a default value.
# It returns the sum of both numbers.
# ---------------------------------------------------

total = 0

def sum(a, b=0):
    print("a:", a)
    print("b:", b)
    total = a + b   # Local variable
    print("Total inside function:", total)
    return total


n = sum(5, 7)
print("Total outside the function:", n)
