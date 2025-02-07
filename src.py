

class Book():
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    
    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, year: {self.year}, amount of pages: {self.pages}"
    

class BookCollection():
    def __init__(self, collection = []):
        self.collection = collection

    def add_book(self, book : Book):
        self.collection.append(book)
        
    def list_books(self):
        print(*[str(x) for x in self.collection], sep="\n")
        
    def __str__(self):
        return "All titles: " + ", ".join([x.title for x in self.collection])

book1 = Book("meow", "cat", 1696, 69)
book2 = Book("woof", "dog", 1420, 222)
col1 = BookCollection()
col1.add_book(book1)
col1.add_book(book2)
col1.list_books()
print(str(col1))