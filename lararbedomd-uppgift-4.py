# Bibliotekssystem

import databas

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        databas.lagg_till_bok(title, author, year)

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
        for loaned_book in self.loaned_books:
            if loaned_book.title == book.title:
                print("Boken är redan utlånad.")
                return

        # Lägg till boken i listan över utlånade böcker
        self.loaned_books.append(LoanedBook(book.title, book.author, book.year, loaner, None))
        print(loaner + " har lånat boken " + book.title + ".")

    def return_book(self, loaner, book):
        # Kontrollera om användaren faktiskt har lånat boken
        for loaned_book in self.loaned_books:
            if loaned_book.title == book.title and loaned_book.loaner == loaner:
                self.loaned_books.remove(loaned_book)
                print("Boken har återlämnats.")
                return

        print("Användaren har inte lånat den boken.")

    def show_all_books(self):
        print("Biblioteket har följande böcker:")
        books = databas.visa_alla_bocker()
        for book in books:
            print("- " + book[1] + " av " + book[2] + " (" + str(book[3]) + ")")

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

def main():
    # Skapa databas och lägg till några böcker
    databas.skapa_databas()

    # Initiera biblioteket
    library = Library([], [], [])
    
    # Initiera alla böcker
    books = [
        Book("Riddaren i våtdräkt", "John Doe", 2014),
        Book("Alfabetet på norska", "Tord Tordsson", 2003),
        Book("Harry Potta", "Joe Mama", 2024)
    ]

    while True:
        # Visa menyn
        print_menu(["Registrera ny låntagare", "Låna bok", "Återlämna bok", "Visa alla böcker", "Avsluta"])
        choosen_alternative = input("Välj ett alternativ: ")
        
        if choosen_alternative == "0":
            member = add_member()
            library.members.append(member)
            print("Låntagare registrerad: " + member.name)
        elif choosen_alternative == "1":
            loaner_name = input("Ange ditt namn: ")
            book_title = input("Ange boktitel: ")
            
            # Hitta låntagaren och boken
            loaner = next((m for m in library.members if m.name == loaner_name), None)
            book = next((b for b in books if b.title == book_title), None)

            if loaner and book:
                library.loan_book(loaner.name, book)
            else:
                print("Låntagare eller bok hittades inte.")
        elif choosen_alternative == "2":
            loaner_name = input("Ange ditt namn: ")
            book_title = input("Ange boktitel: ")

            # Hitta låntagaren och boken
            loaner = next((m for m in library.members if m.name == loaner_name), None)
            book = next((b for b in books if b.title == book_title), None)

            if loaner and book:
                library.return_book(loaner.name, book)
            else:
                print("Låntagare eller bok hittades inte.")
        elif choosen_alternative == "3":
            library.show_all_books()
        elif choosen_alternative == "4":
            print("Avslutar programmet.")
            break

main()
