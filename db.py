#! python

import sqlite3


conn = sqlite3.connect('sde.sqlite')
curs = conn.cursor()

if __name__ == "__main__":
	curs.execute('''SELECT * from invTypes where typeID < 1000''')
	print(curs.fetchone())
