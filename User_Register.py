import json

# File to store user data
USER_FILE = "users.json"

# Function to load existing users
def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save users
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Function to register a new user
def register_user():
    users = load_users()

    print("Welcome to My-Sports Online Store - User Registration")

    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try again.")
        return
    
    password = input("Enter a password: ")
    users[username] = {"password": password}
    
    save_users(users)
    print(f"User '{username}' registered successfully!")

# Run the registration process
if __name__ == "__main__":
    register_user()

