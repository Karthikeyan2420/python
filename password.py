# Dictionary to store usernames and passwords
passwords = {}

def add_password(username, password):
    if username in passwords:
        print(f"Username '{username}' already exists. Please choose another username.")
    else:
        passwords[username] = password
        print(f"Password for '{username}' added successfully.")

def check_password(username, password):
    if username in passwords and passwords[username] == password:
        print(f"Password for '{username}' is correct.")
    else:
        print("Invalid username or password.")

def change_password(username, old_password, new_password):
    if username in passwords and passwords[username] == old_password:
        passwords[username] = new_password
        print(f"Password for '{username}' changed successfully.")
    else:
        print("Invalid username or password. Cannot change password.")

# Example usage
add_password("user1", "password123")
check_password("user1", "password123")
check_password("user1", "password456")

change_password("user1", "password123", "newpassword456")
check_password("user1", "password123")
check_password("user1", "newpassword456")
