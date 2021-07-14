#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()
Items = ["Item1", "Item2", "Item3"]


@app.get("/")
def home():
    return {"Hello": "FastAPI"}


@app.get("/items")
def getAllQuizes():
    returnvalue = "{"
    for x in range(len(Items)):
        returnvalue = returnvalue + Items[x]
    returnvalue = returnvalue + "}"
    return returnvalue
