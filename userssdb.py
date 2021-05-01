import sqlite3

con = sqlite3.connect("users11.db")
print("Database opened successfully")

con.execute("create table hello1(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, vno TEXT NOT NULL, phno TEXT NOT NULL )")

print("Table created successfully")

con.close()