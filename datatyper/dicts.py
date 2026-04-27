dict = {
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2021
}

def return_tuple(name, age):
    return (name, age)

def menu():
    dict = {}

    while True:
        username = input("Username:")
        score = int(input("Score:"))
        dict["username"] = username
        dict["score"] = score
        print(dict)

def menu2():
    user_data = {}
    while True:
        username = input("Username: ")
        if username.lower() == "quit":
            break
        try:
            score = int(input("Score: "))
            user_data["username"] = username
            user_data["score"] = score
            print(f"Stored: {user_data}")
        except ValueError:
            print("Invalid score. Please enter a number.")


def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")

d = {"name": "Alice", "age": 30, "city": "New York"}
print_dict(d)