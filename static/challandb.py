import sqlite3

con = sqlite3.connect("challan1.db")
print("Database opened successfully")

con.execute("create table busys(id INTEGER PRIMARY KEY AUTOINCREMENT, vno TEXT NOT NULL, viol TEXT NOT NULL, amt INTEGER NOT NULL )")

print("Table created successfully")

con.close()