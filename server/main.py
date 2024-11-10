from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def root():
    print('get!!')
    return {"message": "ciao"}


@app.put("/", tags=["root"])
async def update_todo(body: dict) -> dict:
    print('put!!')
    print(body)
    return {"message": "ciao"}


@app.get("/ciao")
async def root():
    print('running!!')
    return {"message": "Ciao World"}
