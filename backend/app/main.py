# app
# main.py

#bibliotecs
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import sys
import subprocess

#modules
from routes import routers
# from database import init_db

#venv
venv_dir = "venv"

def create_venv():
    print("Создаю виртуальное окружение...")
    subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

def install_requirements():
    print("Устанавливаю зависимости...")
    
    if os.name == "nt":  # Windows
        pip = os.path.join(venv_dir, "Scripts", "pip")
    else:  # Linux / Mac
        pip = os.path.join(venv_dir, "bin", "pip")
    subprocess.check_call([pip, "install", "-r", "requirements.txt"])
    
def main():
    if not os.path.exists(venv_dir):
        create_venv()
        install_requirements()
        print("Готово! Перезапусти программу.")
        return


#core
app = FastAPI()


os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# init_db()
for router in routers:
    app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


documentary = "\033[35m Documentary: \033[0m \n   \033[34m http://localhost:8000/docs \033[0m"

config = {
    "host": "localhost",
    "post": 8000
}

if __name__ == "__main__":
    main()
    uvicorn.run("main:app", reload=True, host= config["host"], port=config["post"])

print(documentary)
