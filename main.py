import json


# Function to Add Password
def add_password():

    website = input("Enter Website Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    data = {
        "website": website,
        "username": username,
        "password": password
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
                    print("----------------------------")

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
                    item["password"] = input("Enter New Password: ")

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


# Main Menu
while True:

    print("\n========== PASSWORD MANAGER ==========")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Exit")

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
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")