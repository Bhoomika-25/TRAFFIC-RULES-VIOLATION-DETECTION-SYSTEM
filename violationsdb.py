import sqlite3

con = sqlite3.connect("vio1.db")
print("Database opened successfully")

con.execute("create table culprits (id INTEGER PRIMARY KEY AUTOINCREMENT, vno TEXT NOT NULL, viol TEXT NOT NULL)")

print("Table created successfully")

con.close()