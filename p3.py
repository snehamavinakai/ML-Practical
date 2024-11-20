import re

def validate_email(email):
    # Update email pattern to correct issues and support various top-level domains
    pattern = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone_number(phone_number):
    # E.164 format (international phone number), which can be preceded by an optional '+'
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, phone_number) is not None

def validate_password(password):
    # Updated password pattern to allow special characters
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=]{8,}$'
    return re.match(pattern, password) is not None

def main():
    print("Welcome to the user validation program")
    # Validate email
    email = input("Enter your email address: ")
    if validate_email(email):
        print("Email is valid")
    else:
        print("Invalid email address")
    
    # Validate phone number
    phone_number = input("Enter your phone number: ")
    if validate_phone_number(phone_number):
        print("Phone number is valid")
    else:
        print("Invalid phone number")
    
    # Validate password
    password = input("Enter your password: ")
    if validate_password(password):
        print("Password is valid")
    else:
        print("Invalid password. Make sure that you use at least one uppercase letter, one lowercase letter, one digit, and have at least 8 characters.")

if __name__ == "__main__":
    main()
