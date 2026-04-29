# Bibliotekssystem

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class ChildrensBook(Book):
    def __init__(self, title, author, year, age_recommendation, subject):
        super().__init__(title, author, year)
        self.age_recommendation = age_recommendation
        self.subject = subject

class Member:
    def __init__(self, name, age, late_fees):
        self.name = name
        self.age = age
        self.late_fees = late_fees

class Library:
    def __init__(self, members, books, loaned_books):
        self.members = members
        self.books = books
        self.loaned_books = loaned_books
    
    def loan_book(self, loaner, book):
        # Kontrollera om boken redan är utlånad
        pass

    def return_book(self, loaner, book):
        # Kontrollera om användaren faktiskt har lånat boken
        pass

class LoanedBook(Book):
    def __init__(self, title, author, year, loaner, return_date):
        super().__init__(title, author, year)
        self.loaner = loaner
        self.return_date = return_date

def add_member(): 
    name = str(input("Ange ditt namn:"))
    age = int(input("Ange din ålder:"))

    return Member(name, age, 0)

def print_menu(alternatives):
    i = 0
    while i < len(alternatives):
        print(str(i) + ". " + alternatives[i])
        i += 1

alternatives = ["Registrera ny låntagare", "Låna bok", "Återlämna bok"]
print_menu(alternatives)

# Initiera alla böcker --> Hur initierar vi olika typer av böcker?
books = [
    Book("Riddaren i våtdräkt", "John Doe", 2014),
    ChildrensBook("Alfabetet på norska", "Tord Tordsson", 2003, "3+", "Språk"),
    Book("Harry Potta", "Joe Mama", 2024)
]