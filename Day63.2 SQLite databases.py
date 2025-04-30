import sqlite3
db = sqlite3.connect("book-collection.db")

# cursor creation
cursor = db.cursor()

# Table Creation
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(20) NOT NULL, rating FLOAT NOT NULL)")

# Data insertion to database
cursor.execute("INSERT INTO books VALUES(1,'Harry Potter', 'J.K. Rowling', '9.3')")
db.commit()