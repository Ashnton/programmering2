def show_menu():
    print("1. Enter your name and age")
    print("2. Show when you will turn 100")
    print("3. Exit")

def calculate_year_to_turn_100(current_year, age):
    return current_year + (100 - age)

def main():
    name = ""
    age = 0

    while True:
        show_menu()
        input_choice = input()
        if (input_choice == "1"):
            name = input("Enter name: ")
            age = int(input("Enter age: "))
        elif (input_choice == "2"):
            if (name == "" or age == 0):
                print("Please enter your name and age first.")
            else:
                print(name + ", you will turn 100 in the year " + str(calculate_year_to_turn_100(2026, age)))
        elif (input_choice == "3"):
            break
        else:
            print("Invalid choice, please try again.")

main()