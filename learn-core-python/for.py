# ---------------------------------------------------
# Program 1: Monthly Expense Calculation
# This program calculates and prints the total expense
# by iterating through a list of monthly expenses.
# ---------------------------------------------------

exp = [2340, 2500, 2100, 3100, 2980]
total = 0

for i in range(len(exp)):
    print("Month:", i + 1, "Expense:", exp[i])
    total = total + exp[i]

print("Total Expense:", total)


# ---------------------------------------------------
# Program 2: Key Location Search
# This program searches for a key in different locations.
# If the key is found, it stops searching using 'break'.
# ---------------------------------------------------

key_location = "chair"
locations = ["garage", "living room", "chair", "closet"]

for location in locations:
    if location == key_location:
        print("Key is found in:", location)
        break
    else:
        print("Key is not found in:", location)


# ---------------------------------------------------
# Program 3: Square of Odd Numbers
# This program prints the square of only odd numbers
# between 1 and 5 using 'continue' to skip even numbers.
# ---------------------------------------------------

for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i * i)


# ---------------------------------------------------
# Program 4: While Loop Example
# This program prints numbers from 1 to 5
# using a while loop.
# ---------------------------------------------------

i = 1
while i <= 5:
    print(i)
    i = i + 1
