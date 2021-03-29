#! python

import sqlite3


sde_conn = sqlite3.connect('sde.sqlite')
scurs = sde_conn.cursor()

data_conn = sqlite3.connect('data.sqlite')
dcurs = data_conn.cursor()

def get_typename_by_id(id):
    curs.execute('''SELECT typeName from invTypes where typeID = ?''', (id,))
    return curs.fetchone()

if __name__ == "__main__":
    pass
