import psycopg2

connect = psycopg2.connect(database = 'student_db.db',
                           user = 'postgre',
                           host = 'localhost',
                           password = 'postgre',
                           port = '5432')


cur = conn.cursor()

cur.execute("""CREATE TABLE Student (
 id INT ,
 name TEXT,
 email_id TEXT,
 city TEXT
 )""")
conn.commit()
conn.close()



# retrieving data
cur.execute("""SELECT * FROM Student""")
rows = cur.fetchall()
for row in rows:
    print "ID = {} ".format(row[0])
    print "NAME = {}".format(row[1])
    print("EMAIL = {}".format(row[2]))
    print("CITY = {}".format(row[3]))
