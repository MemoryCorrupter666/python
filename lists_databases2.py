import MySQLdb

connect = MySQLdb.connect('localhost', 'root', '', 'games')
db = connect.cursor()
db.execute("SELECT COUNT(gender) FROM customers where gender = 'M'")
for (gender) in db:
    print(gender)

db.close()
