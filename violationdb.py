import sqlite3

con = sqlite3.connect("userlogin123.db")
print("Database opened successfully")

con.execute("create table violatedusers123 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, vehicleno TEXT NOT NULL, violation TEXT NOT NULL )")

print("Table created successfully")

con.close()