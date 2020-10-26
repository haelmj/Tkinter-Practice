import sqlite3

# create connection to database
def connect():
    with sqlite3.connect('books.db') as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY, 
            title text,
            author text,
            year integer,
            isbn integer)""")

# insert records to database
def insert(title, author, year, isbn):
    with sqlite3.connect('books.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))

# fetch records in database
def view():
    with sqlite3.connect('books.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM book')
        rows=cur.fetchall()
    return rows

# search database
def search(title="", author="", year="", isbn=""):
    with sqlite3.connect('books.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=cur.fetchall()
    return rows

#delete record
def delete(id):
    with sqlite3.connect('books.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()

# update record
def update(id, title, author, year,isbn):
    with sqlite3.connect('books.db') as conn:
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn,id))
        conn.commit()


connect()

