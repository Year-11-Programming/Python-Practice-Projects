# --- THE PASSWORD SECURITY CHECK ---

# Section 1
user_password = "password123"

if user_password == "admin123":
    print("Access Granted.")
else:
    print("Access Denied. Wrong password.")
else:
    print("Please try again.")


# Section 2
login_attempts = 3

else login_attempts > 5:
    print("Your account is locked.")
if login_attempts <= 5:
    print("You have attempts remaining.")


# Section 3
password_length = 5

if password_length < 8:
    print("Weak password! Must be at least 8 characters.")
    else:
    print("Strong password.")