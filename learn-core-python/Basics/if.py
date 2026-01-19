# ---------------------------------------------------
# Program: Cuisine Finder
# This program checks which cuisine a dish belongs to.
# The user enters a dish name, and the program matches
# it with predefined cuisine lists.
# ---------------------------------------------------

# Lists of dishes for each cuisine
indian = ["samosa", "daal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

# Take dish name input from user
dish = input("Enter a dish name: ").lower()

# Check which cuisine the dish belongs to
if dish in indian:
    print("Indian Cuisine")
elif dish in chinese:
    print("Chinese Cuisine")
elif dish in italian:
    print("Italian Cuisine")
else:
    print("Please enter a valid dish name")
