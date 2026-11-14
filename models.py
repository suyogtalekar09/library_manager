
from abc import ABC, abstractmethod


class LibraryItem(ABC):

    total_items = 0                     # class attribute, shared by every item

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True         # Private
        LibraryItem.total_items += 1    # update the class attribute via the class name

    def is_available(self):
        return self.__available

    def mark_borrowed(self):
        self.__available = False
        
    def mark_returned(self):
        self.__available = True
        
    @abstractmethod
    def late_fee(self, days_late):
        pass  




class Book(LibraryItem):
    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        
    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE
    
    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"


class Magazine(LibraryItem):
    DAILY_RATE = 1
    
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        
    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE
    
    def describe(self):
        return f"Magazine: {self.title} by {self.author} (ID {self.item_id})"


class DVD(LibraryItem):
    DAILY_RATE = 5
    
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        
    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE
    
    def describe(self):
        return f"DVD: {self.title} by {self.author} (ID {self.item_id})"



class Member:
    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []  


    def borrow(self, item):
        if not item.is_available():
            raise ValueError("Item is not available for borrowing.")
        
        if len(self.__borrowed) >= self.max_items:
            raise ValueError("You have reached the maximum number of items you can borrow.")
        
        item.mark_borrowed()
        self.__borrowed.append(item)


    def return_item(self, item, days_late=0):
        if item not in self.__borrowed:
            raise ValueError("Item is not in the list of borrowed items.")

        item.mark_returned()
        self.__borrowed.remove(item)
        return item.late_fee(days_late)


    def borrowed_titles(self):
        return [item.title for item in self.__borrowed]