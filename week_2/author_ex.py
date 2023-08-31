class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def publish(self, title):
        self.books.append(title)
    
    def __str__(self):
        titles = ", ".join(self.books) or "No published books"
        return f"Author name: {self.name}\nPublished books: {titles}"


author1 = Author("John Smith")

author1.publish("The Book of John")
author1.publish("The great fall")



print(author1)