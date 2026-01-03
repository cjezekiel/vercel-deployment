from fastapi import FastAPI


app = FastAPI()


db = [
    { "name": "Noma", "age": 23 },
    { "name": "Alvon", "age": 16 },
    { "name": "Pinto", "age": 32 },
    { "name": "Dona", "age": 38 },
    { "name": "Cairo", "age": 17 },
    { "name": "CJ", "age": 25 }
]


@app.get("/")
async def home_root():
    return db

@app.get("/deploy")
async def home_root():

    return {"message": "Render Deploy"}
