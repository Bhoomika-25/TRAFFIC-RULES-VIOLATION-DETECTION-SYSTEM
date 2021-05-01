import sqlite3

con = sqlite3.connect("login3.db")
print("Database opened successfully")

con.execute("create table users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)")

print("Table created successfully")

con.close()