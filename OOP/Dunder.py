class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented
    



book1 = Book("The Alchemist", "Paulo Coelho", 208)
book2 = Book("The Alchemist", "Paulo Coelho", 208)
book3 = Book("Atomic Habits", "James Clear", 320)

# __str__
print(book1)

# __repr__
print(repr(book1))

# __len__
print(len(book1))

# __eq__
print(book1 == book2)  # True
print(book1 == book3)  # False

# __add__
print(book1 + book3)   # 208 + 320