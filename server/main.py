# uvicorn main:app --host 0.0.0.0 --port 8000 --reload 
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

X = []; Y = []; Z = []
app = FastAPI()

class myServer():
    def __init__(self):

        origins = [
            # "http://localhost:3000",
            # "localhost:3000",
            # "http://192.168.1.44:3000",
            # "192.168.1.44:3000",
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

        @app.post("/acc")
        async def acc(x: float = Form(...), y: float = Form(...), z: float = Form(...)):
            X.append(x)
            with open("x.txt", "a") as file:
                file.write(f"{x:.2f}\n")  # Appends the float formatted to 2 decimal places
            
            Y.append(y)
            with open("y.txt", "a") as file:
                file.write(f"{y:.2f}\n")  
        
            Z.append(z)
            with open("z.txt", "a") as file:
                file.write(f"{z:.2f}\n")  

            return {"message": "done"}
   
myServer()