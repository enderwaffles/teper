
# app
# main.py

#bibliotecs
from fastapi import FastAPI

#modules
from routes import routers
from database import init_db



#core
app = FastAPI()

init_db()
for router in routers:
    app.include_router(router)


