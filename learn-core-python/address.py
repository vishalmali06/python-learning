book = {}

book["tom"] = {
    "name": "Tom",
    "address": "123 Main Street",
    "phone": "555-555-556",
}

book["bob"] = {
    "name": "Bob",
    "address": "124 Main Street",
    "phone": "555-555-557",
}

import json

s = json.dumps(book)
with open('book.json', 'w') as f:
    f.write(s)

f = open('book.json', 'r')
s = f.read()
books = json.loads(s)
# print(books)
# print(books["tom"]["phone"])

for person in books:
    print(books[person])
