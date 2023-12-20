print("Bismilla Hir Rahman Nir Raheem")
"""
I am not using database for now..
this code is only to check code_flexibility


"""

import csv
import hashlib
import getpass
from random import randint
import re

CSV_FILE = "codeFlexer.csv"
MIN_MOBILE_DIGITS = 10
MIN_PASSWORD_LENGTH = 8
PASSWORD_PATTERN = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$')


def read_csv():
    try:
        with open(CSV_FILE, "r") as db:
            return list(csv.DictReader(db))
    except FileNotFoundError:
        return []


def write_csv(rows):
    with open(CSV_FILE, "w", newline="") as db:
        headers = ["UserName", "MobileNo", "Passwrd"]
        writer = csv.DictWriter(db, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def is_mobile_unique(mobile, rows):
    return all(int(row["MobileNo"]) != mobile for row in rows)


def is_user_unique(username, rows):
    return all(row["UserName"] != username for row in rows)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_new_user():
    db_reader = read_csv()

    username = input("Name: ")
    if is_user_unique(username, db_reader):
        mobile_no = get_valid_mobile_number(db_reader)
        password = get_valid_password()
        hashed_password = hash_password(password)

        db_reader.append({"UserName": username, "MobileNo": mobile_no, "Passwrd": hashed_password})
        write_csv(db_reader)

        return "Account created"
    else:
        return "Account exists"


def get_valid_mobile_number(rows):
    while True:
        try:
            mobile_no = int(input("Mobile No: "))
            if len(str(mobile_no)) == MIN_MOBILE_DIGITS:
                if is_mobile_unique(mobile_no, rows):
                    return mobile_no
                else:
                    response = input(f"The given MobileNo {mobile_no} has been taken already.\nContinue with this number? Y/N: ")
                    if response.upper() == "Y":
                        return mobile_no
                    elif response.upper() == "N":
                        continue
                    else:
                        print("Use only Y/N")
            else:
                print("10-digit number needed\nDon't use country code.")
        except ValueError:
            print("Invalid input, use numbers.")


def get_valid_password():
    while True:
        password = getpass.getpass("Password: ")
        if len(password) >= MIN_PASSWORD_LENGTH and PASSWORD_PATTERN.match(password):
            confirm_password = getpass.getpass("Confirm Password: ")
            if password == confirm_password:
                return password
            print("Passwords do not match.")
        else:
            print("Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")


def forgot(mobile, reset_password=False):
    db_reader = read_csv()

    for row in db_reader:
        if int(row["MobileNo"]) == mobile:
            if not reset_password:
                print(f"Authentication ID: {row['UserName']}")
            else:
                reset_password_flow(row)
                break


def reset_password_flow(row):
    while True:
        otp = randint(10000, 99999)
        print(otp)
        user_otp = input("OTP: ")
        if otp == int(user_otp):
            new_password = get_valid_password()
            confirm_new_password = getpass.getpass("Confirm New Password: ")
            if new_password == confirm_new_password:
                row["Passwrd"] = hash_password(new_password)
                write_csv(read_csv())
                print("Password reset successful.")
                break
            else:
                print("Passwords do not match.")
        else:
            print("Invalid OTP. Try again.")


def authenticate_user():
    db_reader = read_csv()

    username = input("User Name: ")
    for row in db_reader:
        if row["UserName"] == username:
            password = getpass.getpass("Password: ")
            hashed_password = hash_password(password)
            if row["Passwrd"] == hashed_password:
                return "Credentials matched. You now have complete access to this account."
            return "Incorrect password."

    if not any(row["UserName"] == username for row in db_reader):
        print("User does not exist.")
        response = input("If you want to join our community, Y/N: ")
        if response.upper() == "Y":
            return create_new_user()
        return "Have a Good Day."


def load_page():
    try:
        while True:
            choice = int(input("""
Account Manager..
-------------------
1. Want To Join Our Community
2. Want To Access Your Account
3. Forgot Your Authentication ID
4. Forgot Your Password
5. Exit
$. """))
            if choice == 1:
                print(create_new_user())
            elif choice == 2:
                print(authenticate_user())
            elif choice == 3:
                mobile_no = int(input("Mobile No: "))
                forgot(mobile_no)
            elif choice == 4:
                mobile_no = int(input("Mobile No: "))
                forgot(mobile_no, reset_password=True)
            elif choice == 5:
                print("\t Have A Good Day..")
                break
            else:
                print("Wrong input")
    except ValueError as error:
        print(f"{error}: invalid input, use int()")


if __name__ == "__main__":
    load_page()
