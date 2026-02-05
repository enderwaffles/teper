
#app
#run.py

#bibliotecs
import uvicorn

from fastapi.middleware.cors import CORSMiddleware

#modules
from main import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
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
    uvicorn.run("main:app", reload=True, host= config["host"], port=config["post"])

print(documentary)

