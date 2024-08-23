import json
import os
import re 
def load_data(file_path='user_auth.json'):
    absolute_path = os.path.abspath(file_path)
    print(f"Attempting to load data from: {absolute_path}")
    try:
        with open(absolute_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {absolute_path}")
        return {"users": []}
    except json.JSONDecodeError:
        print("Error decoding JSON. The file might be corrupted.")
        return {"users": []}

def save_data(data, file_path='user_auth.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def check_user_credentials(username, password):
    data = load_data()
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return True
    return False  
        
def adding_user(username, password, email):
    data = load_data()
    new_user = {
        "username": username,
        "password": password,
        "email": email
    }
    data["users"].append(new_user)
    save_data(data)
    return True

def validatingEmail(toBeTested):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, toBeTested))
