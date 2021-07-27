#uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Hello": "FastAPI"}


@app.get("/quizzes")
def getAllQuizes():
    con = sqlite3.connect('Quiz.db')
    cur = con.cursor()
    returnvalue = "["
    for row in cur.execute('SELECT name FROM quiz'):
        returnvalue = returnvalue + '{ "name": "' + row[0] +'"}, '
    returnvalue = returnvalue[:-2] + "]" # last space and comma
    con.close()
    return returnvalue


@app.get("/quiz/{quizid}")
def getAllQuizes(quizid: str):
    con = sqlite3.connect('Quiz.db')
    cur = con.cursor()
    returnvalue = "{"
    for row in cur.execute("SELECT * FROM quiz WHERE name='"+quizid+"';"): # Yes I know SQL Injection {quizid}
        fullquiz = ""
        for col in row:
            fullquiz = fullquiz + " " + col
        returnvalue = returnvalue + fullquiz
    returnvalue = returnvalue + "}"
    return returnvalue