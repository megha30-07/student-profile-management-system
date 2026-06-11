import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        marks REAL
    )
    """)

    conn.commit()
    conn.close()