import sqlite3

conn = sqlite3.connect('exercise2.sqlite')
cur = conn.cursor()

#empty out the data befor each run
cur.execute('DROP TABLE IF EXISTS Counts')

#longer so using triple quotes
cur.execute('''CREATE TABLE Counts (org TEXT,
count INTEGER)''')

fname = input('Enter file name:')
if (len(fname)<1): fname = 'mbox.txt'
fh=open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    email = email.split('@')
    org = email[1]
#replace ? with email -> (emil,) is an one-tuple
    cur.execute('SELECT count FROM Counts WHERE org=?', (org,))

    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org,count)
            VALUES(?,1)''', (org,))
    else:
        cur.execute('''UPDATE Counts SET count = count+1
            WHERE org=?''', (org,))

    conn.commit()

sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(row[0],row[1])

#close connection
cur.close()
