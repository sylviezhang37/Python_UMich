import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

#longer so using triple quotes
cur.execute('''CREATE TABLE Counts (email TEXT,
count INTEGER)''')

.
.
.
#replace ? with email -> (emil,) is an one-tuple
cur.execute('SELECT count FROM Counts WHERE email=?', (email,))
#
row = cur.fetchone()
if row is None:
    cur.execute('''INSERT INTO Counts (email,count)
        VALUES(?,1)''', (email,))
else:
    cur.execute('''UPDATE Counts SET count = count+1
        WHERE email = ?''', (email,))

#commmit
conn.commit()

sqlstr = 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0],row[1]))

#close connection
cur.close()
