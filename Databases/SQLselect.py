import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students WHERE id > 1 and id < 4;")
students = cursor.fetchall()

print("Students with ID > 1:")
for student in students:
    print(student)

conn.close()
