# -----------------------------
# List comprehension examples
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7]

# Traditional way to get even numbers
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)

print("Even numbers (loop):", even)

# List comprehension to get even numbers
even = [i for i in numbers if i % 2 == 0]
print("Even numbers (comprehension):", even)

# List comprehension to get square of numbers
sqr_numbers = [i * i for i in numbers]
print("Square of numbers:", sqr_numbers)


# -----------------------------
# Set comprehension examples
# -----------------------------

# Creating a set (duplicates removed automatically)
s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print("Set:", s)

# Set comprehension to get even numbers
even_set = {i for i in s if i % 2 == 0}
print("Even numbers from set:", even_set)


# --------------------------------
# Dictionary comprehension example
# --------------------------------

cities = ["Pune", "New York", "Paris"]
countries = ["India", "USA", "France"]

# zip() combines elements from both lists
z = zip(cities, countries)

print("Zipped object:", z)

# Iterating over zip object
for city_country in z:
    print(city_country)

# Dictionary comprehension using zip
city_country_dict = {
    city: country for city, country in zip(cities, countries)
}

print("City-Country Dictionary:", city_country_dict)
