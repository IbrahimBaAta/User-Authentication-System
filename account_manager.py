print("Bismilla Hir Rahman Nir Raheem")
"""
I am not using database for now..
this code is only to check code_flexibility


"""


from csv import DictWriter, DictReader
from random import randint
import getpass
import bcrypt

CSV_FILE = "code_flexer.csv"


def read_user_data():
    with open(CSV_FILE, "r") as db:
        return list(DictReader(db))


def write_user_data(data):
    with open(CSV_FILE, "a") as db:
        headers = DictWriter(db, fieldnames=["Username", "MobileNo", "HashedPassword"])
        headers.writerow(data)


def create_new_user():
    user_data = read_user_data()
    username = input("Username: ")

    if all(row["Username"] != username for row in user_data):
        mobile_no = input("Mobile No: ")
        while not mobile_no.isdigit() or len(mobile_no) != 10:
            print("Invalid mobile number. Please enter a 10-digit number.")
            mobile_no = input("Mobile No: ")

        if not all(int(row["MobileNo"]) != int(mobile_no) for row in user_data):
            choice = input(f"The given Mobile No {mobile_no} is already taken. Do you want to continue? (Y/N): ")
            if choice.upper() != "Y":
                return "Account creation canceled."

        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm Password: ")

        if password == confirm_password:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            write_user_data({"Username": username, "MobileNo": mobile_no, "HashedPassword": hashed_password})
            return "Account created successfully."
        else:
            return "Passwords do not match."

    return "Username already exists."


def forgot(mobile, reset_password=False):
    user_data = read_user_data()

    for user in user_data:
        if int(user["MobileNo"]) == mobile:
            if not reset_password:
                return f"Authentication ID: {user['Username']}"
            else:
                otp = str(randint(10000, 99999))
                print(f"OTP: {otp}")

                user_otp = input("Enter OTP: ")
                if user_otp == otp:
                    new_password = getpass.getpass("Enter new password: ")
                    confirm_password = getpass.getpass("Confirm new password: ")

                    if new_password == confirm_password:
                        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                        user["HashedPassword"] = hashed_password
                        write_user_data(user_data)
                        return "Password reset successfully."
                    else:
                        return "Passwords do not match."

                return "Invalid OTP. Password reset failed."

    return "Mobile number not found."


def authenticate_user():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    user_data = read_user_data()

    for user in user_data:
        if user["Username"] == username:
            if bcrypt.checkpw(password.encode('utf-8'), user["HashedPassword"]):
                return "Credentials matched. Access granted."
            else:
                return "Incorrect password."
    else:
        return "User does not exist."


def load_page():
    try:
        while True:
            print("""
    Account Manager..
    -------------------
    1. Create a new account
    2. Access your account
    3. Forgot your authentication ID
    4. Forgot your password
    5. Exit""")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                print(create_new_user())
            elif choice == "2":
                print(authenticate_user())
            elif choice == "3":
                mobile_no = input("Enter your mobile number: ")
                print(forgot(int(mobile_no)))
            elif choice == "4":
                mobile_no = input("Enter your mobile number: ")
                print(forgot(int(mobile_no), reset_password=True))
            elif choice == "5":
                print("Exiting the program. Have a good day!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    except ValueError as error:
        print(error, "Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    load_page()
