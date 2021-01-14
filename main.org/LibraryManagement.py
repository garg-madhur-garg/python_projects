import time


class Library:
    books = {"001": "Mogli Adventures", "002": "Hatimtai Adventures", "003": "HC Verma", "004": "NCERT"}
    lenders = {}

    def __init__(self, listofbooks, libraryname):
        self.listofbooks = listofbooks
        self.libraryname = libraryname

    def add_books(self, key, value):
        self.books[key] = value

    def lend_books(self, key, value):
        if key in obj1.books:
            self.lenders[key] = value
        else:
            print("WRONG ID")

    def display_books(self):
        for key, value in self.books.items():
            print(key+" "+value)
        print("\nNOT AVAILABLE")
        for key, value in self.lenders.items():
            print(key+" "+value)

    def return_books(self, key):
        if key in self.lenders:
            del self.lenders[key]
        else:
            print("WRONG ID")


obj1 = Library({"001": "Mogli Adventures", "002": "Hatimtai Adventures", "003": "HC Verma", "004": "NCERT"}, "SmallLibrary")

print("press A for Add Books\npress L for Lend Books\npress D for Display Books\npress R for Return books\n"
      "press Q for Exit")

while 1:

    opt1 = input("option: ").capitalize()

    if opt1 == "A":
        opt2 = input("Enter Book ID: ")
        opt3 = input("Enter Book Name: ")
        obj1.add_books(opt2, opt3)
        time.sleep(1.5)

    elif opt1 == "D":
        obj1.display_books()

    elif opt1 == "L":
        opt4 = input("Enter Your Name: ")
        opt5 = input("Enter Book ID: ")
        obj1.lend_books(opt5, opt4)
        time.sleep(1.5)

    elif opt1 == "R":
        opt6 = input("Enter Book ID: ")
        obj1.return_books(opt6)
        time.sleep(1.5)

    elif opt1 == "Q":
        quit()

    else:
        print("WRONG INPUT")







