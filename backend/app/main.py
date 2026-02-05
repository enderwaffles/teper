
#app
#main.py

#bibliotecs
from fastapi import FastAPI

#modules
from routes import routers
from database import init_db

app = FastAPI()



init_db()
for router in routers:
    app.include_router(router)

@app.get("/")
def root():
    return "Hello world"

@app.get("/about")
def about():
    return "About"


