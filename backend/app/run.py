
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

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host= "localhost", port=8000)
