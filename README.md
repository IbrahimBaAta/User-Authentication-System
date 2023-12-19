# Account Manager

## Overview
This Python script implements a basic account management system that allows users to create accounts, authenticate, and recover account credentials. The user data is stored in a CSV file (`code_flexer.csv`) with fields for username, mobile number, and hashed passwords. The script uses the `bcrypt` library for secure password hashing.

## Features
1. **Create a New Account**
   - Users can create new accounts by providing a unique username, a valid 10-digit mobile number, and a secure password. Passwords are hashed using the bcrypt algorithm for enhanced security.

2. **Access Your Account**
   - Users can authenticate themselves by entering their username and password. The script verifies the credentials against the stored hashed password.

3. **Forgot Your Authentication ID**
   - Users can retrieve their authentication ID (username) by providing their mobile number. An authentication ID is a unique identifier associated with each user.

4. **Forgot Your Password**
   - Users can initiate a password reset by providing their mobile number. The system sends a one-time password (OTP) to the user, and upon successful verification, allows them to set a new password.

5. **Exit**
   - Users can exit the program at any time.

## Usage
1. Run the script (`account_manager.py`).
2. Follow the on-screen prompts to navigate through the account management options.

## Dependencies
- Python 3.x
- bcrypt library

## Installation
1. Clone the repository.
2. Install the required dependencies: `pip install bcrypt`
3. Run the script: `python account_manager.py`

## Note
- Ensure that the CSV file (`code_flexer.csv`) is present in the same directory as the script to store and retrieve user data.
