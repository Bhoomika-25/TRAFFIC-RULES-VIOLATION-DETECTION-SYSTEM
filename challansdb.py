import sqlite3

con = sqlite3.connect("challans.db")
print("Database opened successfully")

con.execute("create table amount(id INTEGER PRIMARY KEY AUTOINCREMENT, vechno TEXT NOT NULL, viola TEXT NOT NULL, amt1 TEXT NOT NULL)")

print("Table created successfully")

con.close()