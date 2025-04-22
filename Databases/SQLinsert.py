import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Insert students
cursor.execute("INSERT INTO students (name) VALUES ('Alice');")
cursor.execute("INSERT INTO students (name) VALUES ('Bob');")

# Insert courses
cursor.execute("INSERT INTO courses (title) VALUES ('Math');")
cursor.execute("INSERT INTO courses (title) VALUES ('History');")

# Insert enrollments
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (1, 1);")  # Alice in Math
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (2, 2);")  # Bob in History

conn.commit()
conn.close()
print("Data inserted.")
