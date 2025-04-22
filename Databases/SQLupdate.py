import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("UPDATE students SET name = 'Alicia' WHERE id = 1;")

conn.commit()
conn.close()
print("Data Updated.")