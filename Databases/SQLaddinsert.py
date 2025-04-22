import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Add more students
students = ['Charlie', 'Diana', 'Eli']
for name in students:
    cursor.execute("INSERT INTO students (name) VALUES (?);", (name,))

# Add more courses
courses = ['Science', 'Art', 'Programming']
for title in courses:
    cursor.execute("INSERT INTO courses (title) VALUES (?);", (title,))

conn.commit()
conn.close()

print("More students and courses inserted.")
