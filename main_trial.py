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

mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Tim", 19))
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Joe", 22))
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Henry", 28))

mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)