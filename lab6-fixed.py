import os
import secrets
import sqlite3

# Fix 1: Environment variable use ki
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Fix 2: Parameterized query use ki (SQL Injection fix)
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

# Fix 3: secrets module use kiya
def generate_otp():
    return secrets.randbelow(900000) + 100000

# Fix 4: Unused variable hata diya
def calculate():
    result = 10 + 20
    return result
