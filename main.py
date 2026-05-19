import json
import random
import string
from datetime import datetime
from getpass import getpass


# Function to Generate Strong Password
def generate_password():

    length = 12

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password


# Function to Check Password Strength
def check_password_strength(password):

    if len(password) < 6:
        return "Weak"

    elif len(password) < 10:
        return "Medium"

    else:
        return "Strong"


# Function to Add Password
def add_password():

    website = input("Enter Website Name: ")

    if website == "":
        print("Website name cannot be empty")
        return

    username = input("Enter Username: ")

    choice = input("Generate Strong Password? (yes/no): ")

    if choice.lower() == "yes":
        password = generate_password()
        print("Generated Password:", password)

    else:
        password = getpass("Enter Password: ")

    strength = check_password_strength(password)

    data = {
        "website": website,
        "username": username,
        "password": password,
        "strength": strength,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

    except:
        passwords = []

    passwords.append(data)

    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

    print("Password Saved Successfully")
    print("Password Strength:", strength)


# Function to View Passwords
def view_passwords():

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

            if len(passwords) == 0:
                print("No passwords stored")

            else:

                print("\n===== SAVED PASSWORDS =====\n")

                for item in passwords:

                    print("Website :", item["website"])
                    print("Username:", item["username"])
                    print("Password:", item["password"])
                    print("Strength:", item["strength"])
                    print("Created :", item["created_at"])
                    print("----------------------------")

                print("Total Passwords Stored:", len(passwords))

    except:
        print("No password file found")


# Function to Search Password
def search_password():

    website = input("Enter Website Name to Search: ")

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

            found = False

            for item in passwords:

                if item["website"].lower() == website.lower():

                    print("\n===== PASSWORD FOUND =====\n")

                    print("Website :", item["website"])
                    print("Username:", item["username"])
                    print("Password:", item["password"])
                    print("Strength:", item["strength"])
                    print("Created :", item["created_at"])

                    found = True
                    break

            if not found:
                print("No password found for this website")

    except:
        print("No password file found")


# Function to Update Password
def update_password():

    website = input("Enter Website Name to Update: ")

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

            found = False

            for item in passwords:

                if item["website"].lower() == website.lower():

                    print("Current Username:", item["username"])
                    print("Current Password:", item["password"])

                    item["username"] = input("Enter New Username: ")

                    new_password = getpass("Enter New Password: ")

                    item["password"] = new_password
                    item["strength"] = check_password_strength(new_password)

                    found = True
                    break

            if found:

                with open("passwords.json", "w") as file:
                    json.dump(passwords, file, indent=4)

                print("Password Updated Successfully")

            else:
                print("Website not found")

    except:
        print("No password file found")


# Function to Delete Password
def delete_password():

    website = input("Enter Website Name to Delete: ")

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

            new_passwords = []
            found = False

            for item in passwords:

                if item["website"].lower() != website.lower():
                    new_passwords.append(item)

                else:
                    found = True

            if found:

                with open("passwords.json", "w") as file:
                    json.dump(new_passwords, file, indent=4)

                print("Password Deleted Successfully")

            else:
                print("Website not found")

    except:
        print("No password file found")


# Function to Display Statistics
def password_statistics():

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

            print("\n===== PASSWORD STATISTICS =====")
            print("Total Passwords Stored:", len(passwords))

    except:
        print("No password file found")


# Main Menu
while True:

    print("\n========== PASSWORD MANAGER ==========")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Password Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        update_password()

    elif choice == "5":
        delete_password()

    elif choice == "6":
        password_statistics()

    elif choice == "7":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
