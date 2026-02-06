
# app
# routes
# home.py

#bibliotexs
from fastapi import APIRouter



#configs
router = APIRouter(prefix="", tags=["home"])



#core
@router.get("/")
def root():
    return {"message": "Hello world"}

@router.get("/about")
def about():
    return {"message": "About"}