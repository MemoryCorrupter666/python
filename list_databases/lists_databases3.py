import MySQLdb

connect = MySQLdb.connect('localhost', 'root', '', 'games')
db = connect.cursor()
db.execute(
    "SELECT customers.firstname ,orders.ordernumber, games.gamename " \
    "FROM customers " \
    "inner join orders on customers.customernumber = orders.customernumber " \
    "inner join orderdetails on orders.ordernumber = orderdetails.ordernumber " \
    "inner join games on orderdetails.gameid = games.gameid " \
    "where customers.firstname = 'dorothy' ")
for (gender) in db:
    print(gender)

db.close()
