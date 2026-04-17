import random

# Hardcoded password
DB_PASSWORD = "supersecret123"

# SQL Injection vulnerability
def get_user(username):
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Weak random number
def generate_otp():
    return random.randint(100000, 999999)

# Unused variable
def calculate():
    unused_count = 0
    result = 10 + 20
    return result
