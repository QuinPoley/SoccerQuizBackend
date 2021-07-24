import sqlite3

con = sqlite3.connect('Quiz.db')
cur = con.cursor()

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE quiz
              (name text, question1 text, answer1 text, question2 text, answer2 text)''')

# Insert a row of data
cur.execute("INSERT INTO quiz VALUES ('EPL Kits','What color is Manchester United home kit?','Red','What color is Liverpool home kit?','Red')")
cur.execute("INSERT INTO quiz VALUES ('EPL Winners','What year did leicester win the epl?','2015','What color is Liverpool home kit?','Red')")
cur.execute("INSERT INTO quiz VALUES ('UEFA Quiz','Who won the UEFA Champions league in 2007?','AC Milan','What color is Liverpool home kit?','Red')")
# Save (commit) the changes
con.commit()

for row in cur.execute('SELECT name FROM quiz'):
        print(row)


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()