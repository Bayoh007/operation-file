# test.py
from operation import add_books, add_member, search_books, books, members

# Test 1: Adding books
print("Testing add_books:")
add_books("001", "The Alchemist", "Paulo Coelho", "fiction", 10)
add_books("002", "Astrophysics for People in a Hurry", "Neil deGrasse Tyson", "non-fiction", 5)
add_books("001", "Duplicate Book", "Author X", "fiction", 5)  # Should fail (duplicate ISBN)
add_books("003", "Unknown Genre Book", "Author Y", "mystery", 3)  # Should fail (invalid genre)

print("\nBooks currently in library:")
for isbn, details in books.items():
    print(isbn, details)

# Test 2: Adding members
print("\nTesting add_member:")
add_member(101, "John Doe", 'jo0231@gmail.com')
add_member(102, "Jane Smith", "jan9239@gmail.com")
add_member(101, "Ibrahim Sow", "sow9248@gmail.com")

print("\nMembers currently in library:")
for member in members:
    print(member)

# Test 3: Searching books
print("\nTesting search_book:")
results = search_books("alchemist")
print("Search results for 'alchemist':", results)

results = search_books("Neil")
print("Search results for 'Neil':", results)

results = search_books("Nonexistent")
print("Search results for 'Nonexistent':", results)
