import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Get student names and course titles using a JOIN
cursor.execute('''
    SELECT students.name, courses.title
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id;
''')

results = cursor.fetchall()
print("Enrollments:")
for student_name, course_title in results:
    print(f"{student_name} is enrolled in {course_title}")

conn.close()
