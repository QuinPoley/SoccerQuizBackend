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
    con = sqlite3.connect('Question.db')
    cur = con.cursor()
    returnvalue = '{ "quiz": [ '
    values = ['"text"', '"A"', '"B"', '"C"', '"D"']
    for row in cur.execute("SELECT question, a, b, c, d FROM questions WHERE quiz='"+quizid+"';"): # Yes I know SQL Injection {quizid}
        fullquiz = "{"
        #col in row
        for i in range(len(row)):
            var = values[i]
            fullquiz = fullquiz + var +':"'+ row[i] +'",'
        returnvalue = returnvalue + fullquiz[:-1] + "},"
    returnvalue = returnvalue[:-1] + "]}"
    return returnvalue