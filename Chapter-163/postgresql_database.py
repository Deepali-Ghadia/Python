import psycopg2

conn = psycopg2.connect("host=localhost dbname=my_database user=my_user password=my_password")

cur = conn.cursor()

cur.execute("CREATE TABLE Student(student_id, name, mobile_number)")

cur.execute("INSERT INTO Student VALUES('S1', 'Student1'),"
            "('S2', 'Student2'),"
            "('S3', 'Student3'),"
            "('S4', 'Student4'),"
            "('S5', 'Student5'),")

conn.commit()

cur.execute("SELECT * FROM Student")
result = cur.fetchall()

print(result)