import pymssql

# specify the variables required to connect to the datatabase
SERVER = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'trial_db.db'

conn = pymssql.connect(server = SERVER, user = USER, password = PASSWORD, database = DATABASE)

cur = conn.cursor()

cur.execute("CREATE TABLE Employee emp_id(emp_id TEXT, emp_name TEXT)")

cur.execute("INSERT INTO Employee VALUES('E1', 'Employee A' ),"
                                        "('E2', 'Employee B'),"
                                        "('E3', 'Employee C')")

cur.commit()

cur.execute("SELECT * FROM Employee")
