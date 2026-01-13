# -----------------------------
# Set creation (duplicates removed)
# -----------------------------

basket = {"apple", "banana", "cherry", "apple", "banana", "cherry", "mango"}

print("Type of basket:", type(basket))
print("Basket items:", basket)


# -----------------------------
# Creating an empty set
# -----------------------------

a = set()        # Correct way to create an empty set
print("Type of a:", type(a))

a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(1)        # Duplicate value (ignored)

print("Set a:", a)


# -----------------------------
# Empty curly braces create a dictionary
# -----------------------------

a = {}
print("Type of {}:", type(a))   # dict, not set


# -----------------------------
# Creating set from list
# -----------------------------

numbers = [1, 2, 3, 4, 5, 3, 4]
unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)

unique_numbers.add(7)
print("After adding 7:", unique_numbers)


# -----------------------------
# frozenset (immutable set)
# -----------------------------

frozen_set = frozenset(numbers)
print("Frozen set:", frozen_set)

# ❌ Not allowed (frozenset is immutable)
# frozen_set.add(8)   # This will raise AttributeError


# -----------------------------
# Membership test
# -----------------------------

x = {"a", "n"}
print("Set x:", x)

print("'a' in x:", "a" in x)
print("'b' in x:", "b" in x)


# -----------------------------
# Iterating over a set
# -----------------------------

for item in x:
    print("Item:", item)


# -----------------------------
# Set operations
# -----------------------------

y = {"a", "g", "n", "h"}

print("Set x:", x)
print("Set y:", y)

print("Union (x | y):", x | y)
print("Intersection (x & y):", x & y)
print("Difference (x - y):", x - y)
print("Symmetric Difference (x ^ y):", x ^ y)

print("Is x a subset of y?", x < y)
