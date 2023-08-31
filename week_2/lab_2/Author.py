class Author:
    def __init__(self, name):
        self.name = name
        self.books = set()
    
    def publish(self, title):
        # if title not in self.books:
        #     print(f"This book {title} has already been published")
        # else:
        #     self.books.add(title)
        
        duplicate = [print(f"This book {title} has already been published") for t in self.books if t.lower() == title.lower()]
        
        if not duplicate:
            self.books.add(title)
        

    def __str__(self):
        titles = ", ".join(self.books) or "No published books"
        return f"Author name: {self.name}\nPublished books: {titles}"


author1 = Author("John Smith")

author1.publish("A")
author1.publish("A")
author1.publish("A")
author1.publish("B")
author1.publish("C")
author1.publish("D")
author1.publish("D")



print(author1)