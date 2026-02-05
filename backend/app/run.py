
#app
#run.py

import uvicorn

from fastapi.middleware.cors import CORSMiddleware

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
