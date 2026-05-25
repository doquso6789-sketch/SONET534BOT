import json
import os

DB_FILE = "data/users.json"

os.makedirs("data", exist_ok=True)

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)


def save_user(user_id):
    with open(DB_FILE, "r") as f:
        users = json.load(f)

    if user_id not in users:
        users.append(user_id)

    with open(DB_FILE, "w") as f:
        json.dump(users, f)
