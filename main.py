from models import Book, Member, Magazine, DVD

# Creating the book class object
book = Book("Python 101", 1, "A. Rao")

#Creating the magazine class object
magazine = Magazine("Python Weekly", 2, "Python.org")

#Creating the DVD class
dvd = DVD("Python Tutorial", 3, "Python.org")

# Creating the member class objects
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book) 
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.borrow(magazine)  # should fail: limit reached
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.return_item(book)  # should fail: not borrowed by Alice
except ValueError as e:
    print("Could not return:", e)

# 3. Polymorphism: one loop, no type checks
items = [book]  
items.append(magazine)
items.append(dvd)

for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
    
# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)