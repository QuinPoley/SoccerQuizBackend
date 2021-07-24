#uvicorn main:app --reload
from fastapi import FastAPI
import sqlite3

con = sqlite3.connect('Quiz.db')
cur = con.cursor()

app = FastAPI()
Items = ["Item1", "Item2", "Item3"]


@app.get("/")
def home():
    return {"Hello": "FastAPI"}


@app.get("/quizzes")
def getAllQuizes():
    returnvalue = "{"
    for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
    returnvalue = returnvalue + "}"
    return returnvalue


@app.get("/quiz/")
def getAllQuizes():
    returnvalue = "{"
    for x in range(len(Items)):
        returnvalue = returnvalue + Items[x]
    returnvalue = returnvalue + "}"
    return returnvalue