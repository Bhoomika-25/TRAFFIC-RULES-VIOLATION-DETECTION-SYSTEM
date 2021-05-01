import sqlite3

con = sqlite3.connect("userlogin1.db")
print("Database opened successfully")

con.execute("create table violatedusersadd1 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, violation VARCHAR(20), vehicleno VARCHAR(20))")

print("Table created successfully")

con.close()