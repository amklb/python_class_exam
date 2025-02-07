import os
import pandas as pd
from time import sleep

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
        print("All books: ")
        print(*[str(x) for x in self.collection], sep="\n")
        
    def __str__(self):
        return "All titles: " + ", ".join([x.title for x in self.collection])
    
    def make_df(self):
        book_list = []
        for book in self.collection:
            book_dict = {}
            book_dict["title"] = book.title
            book_dict["author"] = book.author
            book_dict["year"] = book.year
            book_dict["pages"] = book.pages
            book_list.append(book_dict)
        df = pd.DataFrame(book_list)
        return df

class BookManager():
    def __init__(self):
        self.collection = BookCollection()
        if os.path.exists(".\\saved_collections") == False:
            os.mkdir(".\\saved_collections")

    def menu(self):
        print("Welcome to book manager!")
        while True:
            print("Enter a number to continue:\n 1. Add book\n 2. View titles in collection\n 3. View collection\n 4. Save collection\n 5. Load collection\n 6. View saved collections\n 7. Exit ")
            n = input("Number: ")
            if n == "1": # Add book
                book_data = input("Please enter comma-separated: title, author, year, pages ").split(sep=", ")
                book = Book(book_data[0], book_data[1], book_data[2], book_data[3])
                self.add_book(book)
            elif n == "2": # List titles
                self.list_titles()
            elif n == "3": # List books
                self.list_books()
            elif n == "4": # Save collection
                self.save_collection()
            elif n == "5": # Load collection
                self.load_collection()
            elif n == "6": # View saved collections
                self.list_files()
            elif n == "7": # Exit
                exit(code= 0)
            else:
                print("Incorrect number!")
            sleep(1)



    def add_book(self, book : Book):
        self.collection.add_book(book=book)
    
    def list_books(self):
        self.collection.list_books()

    def list_titles(self):
        print(str(self.collection))
    
    def list_files(self):
        file_list = os.listdir(".\\saved_collections")
        if len(file_list) == 0:
            print("No saved collections found!")
        else:
            print("Saved collections:")
            print(*file_list, sep=", \n")

    def save_collection(self):
        n_saved = len(os.listdir('.\\saved_collections'))
        df = self.collection.make_df()
        df.to_csv(f".\\saved_collections\\collection{n_saved + 1}.csv")
        print("Collection saved!")

    def load_collection(self):
        path = input("Provide filename (from saved_collection folder): ")
        df = pd.read_csv(".\\saved_collections\\" + path)
        self.collection = BookCollection()
        for index, row in df.iterrows():
            book = Book(title=row["title"], author=row["author"], year=row["year"], pages=row["pages"])
            self.add_book(book)
        print("Collection loaded!")

