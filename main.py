#uvicorn main:app --reload
from fastapi import FastAPI
import sqlite3

app = FastAPI()
Items = ["Item1", "Item2", "Item3"]


@app.get("/")
def home():
    return {"Hello": "FastAPI"}


@app.get("/quizzes")
def getAllQuizes():
    con = sqlite3.connect('Quiz.db')
    cur = con.cursor()
    returnvalue = "{"
    for row in cur.execute('SELECT name FROM quiz'):
        returnvalue = returnvalue + row[0] +', '
    returnvalue = returnvalue[:-2] + "}"
    con.close()
    return returnvalue


@app.get("/quiz/")
def getAllQuizes():
    con = sqlite3.connect('Quiz.db')
    cur = con.cursor()
    returnvalue = "{"
    for row in cur.execute("SELECT * FROM quiz WHERE name='EPL Kits';"):
        fullquiz = ""
        for col in row:
            fullquiz = fullquiz + " " + col
        returnvalue = returnvalue + fullquiz
    returnvalue = returnvalue + "}"
    return returnvalue