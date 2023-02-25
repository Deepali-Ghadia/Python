import sqlite3

# establishing connection with the database
conn = sqlite3.connect('Chapter-50/instructors_data.db')

# creating a cursor so that we can execute SQL queries on sqlite
c = conn.cursor()

# adding data to the database
c.execute(""" CREATE TABLE  IF NOT EXISTS instructors(instructor_id text, instructor_name text)""")
c.execute("INSERT INTO instructors VALUES ('I1', 'SAK'),"
                                            "('I2', 'SDJ'),"
                                            "('I3', 'AMK'),"
                                            "('I4', 'AKS')")


# getting value from the database
c.execute("SELECT * FROM instructors")
print(c.fetchone()) # fetches single record

result = c.fetchall()
print(result)