# Funktion: Lägg till en användare
def add_user(users):
    # Ta input från användaren
    username = input("Ange användarnamn: ")
    age = input("Ange ålder: ")
    email = input("Ange e-post: ")
    
    # Spara i dictionary
    user = {
        "username": username,
        "age": age,
        "email": email
    }

    # Appenda dictionaryn till lista över users
    users.append(user)
    return True

# Funktion: Sök efter en användare
def search_user(users):
    # Be användaren skriva in ett sökord (t.ex. namn eller e-post)
    search_input = input("Ange sökord: (namn, e-postadress eller ålder)")

    # Sök i listan efter matchande användare och skriv ut resultat
    j = 0
    # Iterera genom lista. Skriver ut exakta matchningar
    for i in users:
        if (i["username"] == search_input or i["age"] == search_input or i["email"] == search_input):
            print(i["username"] + ", " + i["age"] + ", " + i["email"])
            j += 1
        
    if (j == 0):
        print("Inga matchningar")

            
        
def show_users(users):
    # Sortera användarna efter namn
    sorted_users = sorted(users, key=lambda x: x["username"])
    for i in sorted_users:
        print(i["username"] + ", " + i["age"] + ", " + i["email"])

# Huvudfunktion: Sköter meny och programflöde
def main():
    users = []  # Här lagras användarna som dictionaries
    while True:
        print("\n1. Lägg till användare\n2. Sök användare\n3. Visa alla användare\n4. Avsluta")
        choice = input("Välj ett alternativ: ")
        if choice == "1":
            add_user(users)
        elif choice == "2":
            search_user(users)
        elif choice == "3":
            show_users(users)
        elif choice == "4":
            print("Programmet avslutas.")
            break
        else:
            print("Ogiltigt val, försök igen.")

# Starta programmet
main()
