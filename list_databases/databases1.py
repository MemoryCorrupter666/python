import MySQLdb

connect = MySQLdb.connect('localhost', 'root', '', 'games')
db = connect.cursor()

db.execute("SELECT price, gamename FROM games")

for (price, gamename) in db:
    print('\n')
    print('de game naam: ', gamename)
    print('de game prijs: ', price)

db.close()