Q1 - Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

Ans - LibraryItem is abstract to require every item type to implement its own late_fee() calculation. If DVD omits it, Python will prevent creating a DVD object and raise a TypeError stating that the abstract method is missing.


Q2 - What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Ans - Reading item.__available from outside the class raises an AttributeError because the attribute is private through name mangling. We use is_available() to safely access its value while protecting the internal state from direct modification.

Q3 - What is the difference between LibraryItem.total_items and self.title?

Ans - LibraryItem.total_items is a class attribute shared by all library items, tracking the total number created. self.title is an instance attribute specific to each individual item, storing that item’s title.

