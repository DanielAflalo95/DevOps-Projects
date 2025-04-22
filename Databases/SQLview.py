import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# View all students
cursor.execute("SELECT * FROM students;")
print("Students:", cursor.fetchall())

# View all courses
cursor.execute("SELECT * FROM courses;")
print("Courses:", cursor.fetchall())

# View all enrollments
cursor.execute("SELECT * FROM enrollments;")
print("Enrollments:", cursor.fetchall())

conn.close()
