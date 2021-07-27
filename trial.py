import sqlite3

con = sqlite3.connect('Quiz.db')
cur = con.cursor()


# Create table
cur.execute('''CREATE TABLE quiz
              (name text, description text)''')

# Insert a row of data
cur.execute("INSERT INTO quiz VALUES ('EPLKits','A quiz about Kits of the teams in the english premier league')")
cur.execute("INSERT INTO quiz VALUES ('EPLWinners','A quiz about winners of the epl')")
cur.execute("INSERT INTO quiz VALUES ('UEFAQuiz','A quiz about the champions league')")
# Save (commit) the changes
con.commit()


connection = sqlite3.connect('Question.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE questions
              (question text, a text, b text, c text, d text, answer text, quiz text, number int)''')

# EPL KITS
cursor.execute("INSERT INTO questions VALUES ('What color is Liverpools home kit?','Red', 'White', 'Black', 'Blue', 'Red', 'EPLKits', 1)")
cursor.execute("INSERT INTO questions VALUES ('What color is Manchester Citys home kit?','Red', 'White', 'Yellow', 'Blue', 'Blue', 'EPLKits', 2)")
cursor.execute("INSERT INTO questions VALUES ('What color is Wolvess home kit?','Black', 'Orange', 'Green', 'White', 'Orange', 'EPLKits', 3)")
cursor.execute("INSERT INTO questions VALUES ('What color is Leicester City home kit?','Blue', 'White', 'Purple', 'Black', 'Blue', 'EPLKits', 4)")
cursor.execute("INSERT INTO questions VALUES ('What color is Wolvess home kit?','Black', 'Orange', 'Green', 'White', 'Orange', 'EPLKits', 5)")

# EPL WINNERS
cursor.execute("INSERT INTO questions VALUES ('What team won the premier league 15/16 season?','Red', 'White', 'Black', 'Blue', 'Red', 'EPLWinners', 1)")
cursor.execute("INSERT INTO questions VALUES ('What team won the premier league without a loss 20 years ago and has done nothing of note since?','Arsenal', 'That one', 'Yep', 'Still Arsenal', 'Arsenal', 'EPLWinners', 2)")
cursor.execute("INSERT INTO questions VALUES ('What team has the most premier league titles?','Leicester', 'Manchester United', 'Liverpool', 'Chelsea', 'Manchester United', 'EPLWinners', 3)")
cursor.execute("INSERT INTO questions VALUES ('What team won in 20/21?', 'Chelsea', 'Manchester United', 'Liverpool', 'Manchester City', 'Manchester City', 'EPLWinners', 4)")
cursor.execute("INSERT INTO questions VALUES ('What team won in 19/20?', 'Chelsea', 'Manchester United', 'Liverpool', 'Manchester City', 'Liverpool', 'EPLWinners', 5)")


#UEFA QUIZ
cursor.execute("INSERT INTO questions VALUES ('What team has the most UCL trophies?','Real Madrid', 'Liverpool', 'AC Milan', 'Fulham', 'Real Madrid', 'UEFAQuiz', 1)")
cursor.execute("INSERT INTO questions VALUES ('How many UCL trophies does Arsenal have?','0', 'A', 'B', 'C', '0', 'UEFAQuiz', 2)")
cursor.execute("INSERT INTO questions VALUES ('How many UCL trophies does Juventus have?','0', '1', '2', '4', '2', 'UEFAQuiz', 3)")
cursor.execute("INSERT INTO questions VALUES ('How many UCL trophies does Barcelona have?','5', '6', '8', '4', '5', 'UEFAQuiz', 4)")
cursor.execute("INSERT INTO questions VALUES ('Who is the highest scoring player in UCL history?','Lionel Messi', 'Raul Gonzalez', 'Robert Lewandowski', 'Cristiano Ronaldo', 'Cristiano Ronaldo', 'UEFAQuiz', 5)")


connection.commit()



# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
cursor.close()