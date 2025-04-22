import sqlite3

# Connect to database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
''')

# Create courses table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL
    );
''')

# Create enrollments table with foreign keys
cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id),
        PRIMARY KEY (student_id, course_id)
    );
''')

# Commit and close
conn.commit()
conn.close()

print("All tables created successfully.")