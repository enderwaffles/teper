# app
# main.py

#bibliotecs
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

#modules
from routes import routers
from database import init_db



#core
app = FastAPI()

init_db()
for router in routers:
    app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.mount("/static", StaticFiles(directory="static"), name="static")

documentary = "\033[35m Documentary: \033[0m \n   \033[34m http://localhost:8000/docs \033[0m"

config = {
    "host": "localhost",
    "post": 8000
}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host= config["host"], port=config["post"])

print(documentary)
