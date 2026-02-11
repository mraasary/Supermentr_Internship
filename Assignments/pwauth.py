import hashlib
import os

def hash_password(password):
    """Hash password with salt"""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

def verify_password(stored_password, provided_password):
    """Verify a stored password against provided password"""
    salt = stored_password[:32]
    stored_key = stored_password[32:]
    key = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return key == stored_key

# User registration
print("=== Register ===")
username = input("Enter username: ")
password = input("Enter password: ")
hashed_password = hash_password(password)
print("User registered successfully!\n")

# User login
print("=== Login ===")
login_username = input("Enter username: ")
login_password = input("Enter password: ")

if login_username == username and verify_password(hashed_password, login_password):
    print("Login successful!")
else:
    print("Login failed! Invalid username or password.")