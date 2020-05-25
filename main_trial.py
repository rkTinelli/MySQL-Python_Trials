import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS testdatabase")
mycursor.execute("USE testdatabase")

mycursor.execute("CREATE TABLE IF NOT EXISTS Person "
                 "(name VARCHAR(50), age smallint UNSIGNED,"
                 "personID int PRIMARY KEY AUTO_INCREMENT)")

# Not following best practices for multiple entries
'''
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Tim", 19))
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Joe", 22))
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Henry", 28))
db.commit()
'''

# Adding multiple entries
sql = "INSERT INTO Person (name, age) VALUES (%s, %s)"
val = [
  ('Peter', 15),
  ('Amy', 45),
  ('Hannah', 36),
  ('Michael', 24),
  ('Sandy', 15),
  ('Betty', 5),
  ('Richard', 55),
  ('Susan', 49),
  ('Vicky', 42),
  ('Ben', 65)
]
mycursor.executemany(sql, val)
db.commit()

mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)